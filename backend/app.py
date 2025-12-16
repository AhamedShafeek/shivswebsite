from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
from html_updater import HTMLUpdater
from git_manager import GitManager

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
CORS(app)

# Initialize utilities
html_updater = HTMLUpdater()
git_manager = GitManager()

# Data file paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
REVIEWS_FILE = os.path.join(DATA_DIR, 'reviews.json')
FAQS_FILE = os.path.join(DATA_DIR, 'faqs.json')
GALLERY_FILE = os.path.join(DATA_DIR, 'gallery.json')
REELS_FILE = os.path.join(DATA_DIR, 'reels.json')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Helper functions to load/save data
def load_json(file_path, default=None):
    if default is None:
        default = []
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return default

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Initialize JSON files if they don't exist
if not os.path.exists(REVIEWS_FILE):
    save_json(REVIEWS_FILE, [])
if not os.path.exists(FAQS_FILE):
    save_json(FAQS_FILE, [])
if not os.path.exists(GALLERY_FILE):
    save_json(GALLERY_FILE, [])
if not os.path.exists(REELS_FILE):
    save_json(REELS_FILE, [])

# ========== ROUTES ==========

@app.route('/')
def index():
    return render_template('dashboard.html')

# ========== REVIEW ROUTES ==========

@app.route('/reviews')
def reviews_manager():
    reviews = load_json(REVIEWS_FILE)
    return render_template('reviews.html', reviews=reviews)

@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews = load_json(REVIEWS_FILE)
    return jsonify(reviews)

@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.json
    reviews = load_json(REVIEWS_FILE)
    
    new_review = {
        'id': len(reviews) + 1,
        'name': data.get('name'),
        'initial': data.get('initial'),
        'rating': data.get('rating', 5),
        'time': data.get('time', '3 months ago'),
        'title': data.get('title'),
        'content': data.get('content'),
        'badge': data.get('badge', ''),
        'created_at': datetime.now().isoformat()
    }
    
    reviews.append(new_review)
    save_json(REVIEWS_FILE, reviews)
    
    # Update HTML
    html_updater.update_reviews(reviews)
    
    flash('Review added successfully!', 'success')
    return jsonify({'success': True, 'review': new_review})

@app.route('/api/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    reviews = load_json(REVIEWS_FILE)
    
    for review in reviews:
        if review['id'] == review_id:
            review.update({
                'name': data.get('name', review['name']),
                'initial': data.get('initial', review['initial']),
                'rating': data.get('rating', review['rating']),
                'time': data.get('time', review['time']),
                'title': data.get('title', review['title']),
                'content': data.get('content', review['content']),
                'badge': data.get('badge', review.get('badge', '')),
                'updated_at': datetime.now().isoformat()
            })
            break
    
    save_json(REVIEWS_FILE, reviews)
    html_updater.update_reviews(reviews)
    
    return jsonify({'success': True})

@app.route('/api/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    reviews = load_json(REVIEWS_FILE)
    reviews = [r for r in reviews if r['id'] != review_id]
    save_json(REVIEWS_FILE, reviews)
    
    html_updater.update_reviews(reviews)
    
    return jsonify({'success': True})

# ========== FAQ ROUTES ==========

@app.route('/faqs')
def faqs_manager():
    faqs = load_json(FAQS_FILE)
    return render_template('faqs.html', faqs=faqs)

@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    faqs = load_json(FAQS_FILE)
    return jsonify(faqs)

@app.route('/api/faqs', methods=['POST'])
def add_faq():
    data = request.json
    faqs = load_json(FAQS_FILE)
    
    new_faq = {
        'id': len(faqs) + 1,
        'question': data.get('question'),
        'answer': data.get('answer'),
        'created_at': datetime.now().isoformat()
    }
    
    faqs.append(new_faq)
    save_json(FAQS_FILE, faqs)
    
    html_updater.update_faqs(faqs)
    
    return jsonify({'success': True, 'faq': new_faq})

@app.route('/api/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    data = request.json
    faqs = load_json(FAQS_FILE)
    
    for faq in faqs:
        if faq['id'] == faq_id:
            faq.update({
                'question': data.get('question', faq['question']),
                'answer': data.get('answer', faq['answer']),
                'updated_at': datetime.now().isoformat()
            })
            break
    
    save_json(FAQS_FILE, faqs)
    html_updater.update_faqs(faqs)
    
    return jsonify({'success': True})

@app.route('/api/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    faqs = load_json(FAQS_FILE)
    faqs = [f for f in faqs if f['id'] != faq_id]
    save_json(FAQS_FILE, faqs)
    
    html_updater.update_faqs(faqs)
    
    return jsonify({'success': True})

# ========== GALLERY ROUTES ==========

@app.route('/gallery')
def gallery_manager():
    gallery = load_json(GALLERY_FILE)
    return render_template('gallery.html', gallery=gallery)

@app.route('/api/gallery', methods=['GET'])
def get_gallery():
    gallery = load_json(GALLERY_FILE)
    return jsonify(gallery)

@app.route('/api/gallery', methods=['POST'])
def add_gallery_image():
    data = request.json
    gallery = load_json(GALLERY_FILE)
    
    new_image = {
        'id': len(gallery) + 1,
        'url': data.get('url'),
        'category': data.get('category', 'weddings'),
        'alt': data.get('alt', 'Gallery image'),
        'created_at': datetime.now().isoformat()
    }
    
    gallery.append(new_image)
    save_json(GALLERY_FILE, gallery)
    
    html_updater.update_gallery(gallery)
    
    return jsonify({'success': True, 'image': new_image})

@app.route('/api/gallery/<int:image_id>', methods=['PUT'])
def update_gallery_image(image_id):
    data = request.json
    gallery = load_json(GALLERY_FILE)
    
    for image in gallery:
        if image['id'] == image_id:
            image.update({
                'url': data.get('url', image['url']),
                'category': data.get('category', image['category']),
                'alt': data.get('alt', image['alt']),
                'updated_at': datetime.now().isoformat()
            })
            break
    
    save_json(GALLERY_FILE, gallery)
    html_updater.update_gallery(gallery)
    
    return jsonify({'success': True})

@app.route('/api/gallery/<int:image_id>', methods=['DELETE'])
def delete_gallery_image(image_id):
    gallery = load_json(GALLERY_FILE)
    gallery = [img for img in gallery if img['id'] != image_id]
    save_json(GALLERY_FILE, gallery)
    
    html_updater.update_gallery(gallery)
    
    return jsonify({'success': True})

# ========== REELS ROUTES ==========

@app.route('/reels')
def reels_manager():
    reels = load_json(REELS_FILE)
    return render_template('reels.html', reels=reels)

@app.route('/api/reels', methods=['GET'])
def get_reels():
    reels = load_json(REELS_FILE)
    return jsonify(reels)

@app.route('/api/reels', methods=['POST'])
def add_reel():
    data = request.json
    reels = load_json(REELS_FILE)
    
    new_reel = {
        'id': len(reels) + 1,
        'embed_url': data.get('embed_url'),
        'title': data.get('title', 'Instagram Reel'),
        'created_at': datetime.now().isoformat()
    }
    
    reels.append(new_reel)
    save_json(REELS_FILE, reels)
    
    html_updater.update_reels(reels)
    
    return jsonify({'success': True, 'reel': new_reel})

@app.route('/api/reels/<int:reel_id>', methods=['PUT'])
def update_reel(reel_id):
    data = request.json
    reels = load_json(REELS_FILE)
    
    for reel in reels:
        if reel['id'] == reel_id:
            reel.update({
                'embed_url': data.get('embed_url', reel['embed_url']),
                'title': data.get('title', reel['title']),
                'updated_at': datetime.now().isoformat()
            })
            break
    
    save_json(REELS_FILE, reels)
    html_updater.update_reels(reels)
    
    return jsonify({'success': True})

@app.route('/api/reels/<int:reel_id>', methods=['DELETE'])
def delete_reel(reel_id):
    reels = load_json(REELS_FILE)
    reels = [r for r in reels if r['id'] != reel_id]
    save_json(REELS_FILE, reels)
    
    html_updater.update_reels(reels)
    
    return jsonify({'success': True})

# ========== GIT ROUTES ==========

@app.route('/git/push', methods=['POST'])
def git_push():
    data = request.json
    commit_message = data.get('message', 'Update website content')
    
    try:
        result = git_manager.commit_and_push(commit_message)
        return jsonify({'success': True, 'message': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/git/status', methods=['GET'])
def git_status():
    try:
        status = git_manager.get_status()
        return jsonify({'success': True, 'status': status})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
