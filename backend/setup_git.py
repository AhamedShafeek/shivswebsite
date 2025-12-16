"""
Git Setup Helper for Shiv's Photography Backend

This script helps you initialize and configure Git for your project.
"""

import subprocess
import os
import sys

def run_command(command, cwd=None):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except FileNotFoundError:
        return False, "Command not found"

def check_git_installed():
    """Check if Git is installed"""
    success, output = run_command('git --version')
    if success:
        print(f"✓ Git is installed: {output.strip()}")
        return True
    else:
        print("✗ Git is not installed!")
        print("\nPlease install Git from: https://git-scm.com/downloads")
        return False

def is_git_repo(repo_path):
    """Check if directory is a git repository"""
    success, _ = run_command('git rev-parse --git-dir', cwd=repo_path)
    return success

def init_git_repo(repo_path):
    """Initialize a git repository"""
    if is_git_repo(repo_path):
        print("✓ Already a git repository")
        return True
    
    print("\nInitializing git repository...")
    success, output = run_command('git init', cwd=repo_path)
    if success:
        print("✓ Git repository initialized")
        return True
    else:
        print(f"✗ Failed to initialize git: {output}")
        return False

def configure_git_user(repo_path):
    """Configure git user name and email"""
    print("\n--- Git User Configuration ---")
    
    # Check current configuration
    success, current_name = run_command('git config user.name', cwd=repo_path)
    success2, current_email = run_command('git config user.email', cwd=repo_path)
    
    if success and current_name.strip():
        print(f"Current name: {current_name.strip()}")
        use_current = input("Keep this name? (y/n): ").lower()
        if use_current == 'y':
            name = current_name.strip()
        else:
            name = input("Enter your name: ")
    else:
        name = input("Enter your name: ")
    
    if success2 and current_email.strip():
        print(f"Current email: {current_email.strip()}")
        use_current = input("Keep this email? (y/n): ").lower()
        if use_current == 'y':
            email = current_email.strip()
        else:
            email = input("Enter your email: ")
    else:
        email = input("Enter your email: ")
    
    # Set configuration
    run_command(f'git config user.name "{name}"', cwd=repo_path)
    run_command(f'git config user.email "{email}"', cwd=repo_path)
    
    print(f"✓ Git user configured: {name} <{email}>")
    return True

def add_git_remote(repo_path):
    """Add a git remote repository"""
    print("\n--- Git Remote Configuration ---")
    
    # Check if remote already exists
    success, remotes = run_command('git remote -v', cwd=repo_path)
    
    if success and remotes.strip():
        print("Current remotes:")
        print(remotes)
        add_new = input("\nAdd a new remote? (y/n): ").lower()
        if add_new != 'y':
            return True
    
    print("\nExamples of remote URLs:")
    print("  HTTPS: https://github.com/username/repo-name.git")
    print("  SSH:   git@github.com:username/repo-name.git")
    
    remote_url = input("\nEnter your GitHub repository URL: ").strip()
    
    if not remote_url:
        print("No remote URL provided. Skipping remote setup.")
        return False
    
    remote_name = input("Remote name (default: origin): ").strip() or "origin"
    
    # Try to add remote
    success, output = run_command(f'git remote add {remote_name} {remote_url}', cwd=repo_path)
    
    if success:
        print(f"✓ Remote '{remote_name}' added successfully")
        return True
    elif "already exists" in output.lower():
        print(f"Remote '{remote_name}' already exists. Updating URL...")
        success, _ = run_command(f'git remote set-url {remote_name} {remote_url}', cwd=repo_path)
        if success:
            print(f"✓ Remote '{remote_name}' URL updated")
            return True
    
    print(f"✗ Failed to add remote: {output}")
    return False

def create_gitignore(repo_path):
    """Create a .gitignore file if it doesn't exist"""
    gitignore_path = os.path.join(repo_path, '.gitignore')
    
    if os.path.exists(gitignore_path):
        print("✓ .gitignore already exists")
        return True
    
    print("\nCreating .gitignore file...")
    
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Logs
*.log
"""
    
    try:
        with open(gitignore_path, 'w') as f:
            f.write(gitignore_content)
        print("✓ .gitignore created")
        return True
    except Exception as e:
        print(f"✗ Failed to create .gitignore: {e}")
        return False

def initial_commit(repo_path):
    """Make initial commit"""
    print("\n--- Initial Commit ---")
    
    # Check if there are any commits
    success, _ = run_command('git log -1', cwd=repo_path)
    
    if success:
        print("✓ Repository already has commits")
        return True
    
    make_commit = input("Make an initial commit? (y/n): ").lower()
    
    if make_commit != 'y':
        return False
    
    # Stage all files
    print("Staging files...")
    run_command('git add .', cwd=repo_path)
    
    # Commit
    commit_msg = input("Commit message (default: 'Initial commit'): ").strip() or "Initial commit"
    success, output = run_command(f'git commit -m "{commit_msg}"', cwd=repo_path)
    
    if success:
        print("✓ Initial commit created")
        return True
    elif "nothing to commit" in output.lower():
        print("✓ Nothing to commit (already committed)")
        return True
    else:
        print(f"✗ Commit failed: {output}")
        return False

def main():
    print("=" * 60)
    print("GIT SETUP HELPER - Shiv's Photography")
    print("=" * 60)
    
    # Get repository path (parent of backend folder)
    backend_path = os.path.dirname(os.path.abspath(__file__))
    repo_path = os.path.dirname(backend_path)
    
    print(f"\nRepository path: {repo_path}")
    
    # Step 1: Check if Git is installed
    if not check_git_installed():
        sys.exit(1)
    
    # Step 2: Initialize Git repository
    if not init_git_repo(repo_path):
        sys.exit(1)
    
    # Step 3: Configure Git user
    configure_git_user(repo_path)
    
    # Step 4: Create .gitignore
    create_gitignore(repo_path)
    
    # Step 5: Add remote repository
    has_remote = add_git_remote(repo_path)
    
    # Step 6: Initial commit
    initial_commit(repo_path)
    
    print("\n" + "=" * 60)
    print("GIT SETUP COMPLETE!")
    print("=" * 60)
    
    if has_remote:
        print("\n✓ Your repository is ready to push to GitHub!")
        print("\nNext steps:")
        print("1. Use the admin panel to make changes")
        print("2. Click 'Push to Git' to upload changes")
        print("3. Your website will be updated on GitHub!")
    else:
        print("\n⚠ No remote repository configured.")
        print("\nTo add a remote later, run:")
        print("  git remote add origin https://github.com/username/repo.git")
    
    print("\nYou can now use the admin panel's Git features!")
    print(f"\nAdmin panel: http://localhost:5000")
    
    input("\nPress Enter to exit...")

if __name__ == '__main__':
    main()
