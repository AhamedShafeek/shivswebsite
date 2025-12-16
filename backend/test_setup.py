"""
Test script to verify backend functionality
Run this to test if everything is set up correctly
"""

import os
import sys
import json

def test_imports():
    """Test if all required packages are installed"""
    print("Testing imports...")
    try:
        import flask
        print("✓ Flask installed")
        import flask_cors
        print("✓ Flask-CORS installed")
        from bs4 import BeautifulSoup
        print("✓ BeautifulSoup installed")
        import lxml
        print("✓ lxml installed")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("\nPlease run: pip install -r requirements.txt")
        return False

def test_file_structure():
    """Test if all required files and folders exist"""
    print("\nTesting file structure...")
    
    required_files = [
        'app.py',
        'html_updater.py',
        'git_manager.py',
        'config.py',
        'requirements.txt',
    ]
    
    required_dirs = [
        'data',
        'templates',
        'static'
    ]
    
    all_good = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file} exists")
        else:
            print(f"✗ {file} missing")
            all_good = False
    
    for dir in required_dirs:
        if os.path.exists(dir):
            print(f"✓ {dir}/ directory exists")
        else:
            print(f"✗ {dir}/ directory missing")
            all_good = False
    
    return all_good

def test_data_files():
    """Test if data files are properly initialized"""
    print("\nTesting data files...")
    
    data_files = [
        'data/reviews.json',
        'data/faqs.json',
        'data/gallery.json',
        'data/reels.json'
    ]
    
    all_good = True
    
    for file in data_files:
        if os.path.exists(file):
            try:
                with open(file, 'r') as f:
                    data = json.load(f)
                    print(f"✓ {file} is valid JSON ({len(data)} items)")
            except json.JSONDecodeError:
                print(f"✗ {file} is not valid JSON")
                all_good = False
        else:
            print(f"✗ {file} does not exist")
            all_good = False
    
    return all_good

def test_html_file():
    """Test if main HTML file exists"""
    print("\nTesting HTML file...")
    
    html_path = os.path.join('..', 'index.html')
    
    if os.path.exists(html_path):
        print(f"✓ index.html found")
        file_size = os.path.getsize(html_path)
        print(f"  File size: {file_size:,} bytes")
        return True
    else:
        print(f"✗ index.html not found at {html_path}")
        return False

def test_templates():
    """Test if all template files exist"""
    print("\nTesting template files...")
    
    templates = [
        'templates/dashboard.html',
        'templates/reviews.html',
        'templates/faqs.html',
        'templates/gallery.html',
        'templates/reels.html'
    ]
    
    all_good = True
    
    for template in templates:
        if os.path.exists(template):
            print(f"✓ {template} exists")
        else:
            print(f"✗ {template} missing")
            all_good = False
    
    return all_good

def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("SHIV'S PHOTOGRAPHY BACKEND - SYSTEM TEST")
    print("=" * 50)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("File Structure", test_file_structure()))
    results.append(("Data Files", test_data_files()))
    results.append(("HTML File", test_html_file()))
    results.append(("Templates", test_templates()))
    
    print("\n" + "=" * 50)
    print("TEST RESULTS")
    print("=" * 50)
    
    all_passed = True
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("\n🎉 All tests passed! You're ready to go!")
        print("\nTo start the server, run:")
        print("  python app.py")
        print("\nThen open your browser to:")
        print("  http://localhost:5000")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Make sure you're in the backend directory")
        print("  3. Check that index.html exists in parent directory")
    
    return all_passed

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
