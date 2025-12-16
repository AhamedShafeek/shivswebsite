# Shiv's Photography - Backend Admin Panel

A Flask-based backend system for managing the Shiv's Photography website content. This admin panel allows you to:

- ✨ **Manage Reviews**: Add, edit, and delete customer reviews
- ❓ **Manage FAQs**: Create and manage frequently asked questions
- 🖼️ **Manage Gallery**: Upload and organize gallery images by category
- 🎬 **Manage Reels**: Add Instagram reels and embedded content
- 🚀 **Git Integration**: Automatically push changes to your repository

## Features

- **Dynamic HTML Updates**: Automatically updates the main website HTML when you make changes
- **JSON Data Storage**: All data stored in easy-to-manage JSON files
- **Git Auto-Push**: One-click push to GitHub repository
- **Beautiful UI**: Modern, responsive admin interface built with Tailwind CSS
- **RESTful API**: Full CRUD operations for all content types

## Installation

### 1. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The server will start on `http://localhost:5000`

## Usage

### Access the Admin Panel

1. Open your browser and go to `http://localhost:5000`
2. You'll see the dashboard with options to manage:
   - Reviews
   - FAQs
   - Gallery Images
   - Instagram Reels

### Managing Content

#### Reviews
- Navigate to `/reviews`
- Fill in the form with customer name, rating, review text, etc.
- Click "Add Review" to save
- The HTML file will be automatically updated

#### FAQs
- Navigate to `/faqs`
- Enter question and answer
- Click "Add FAQ" to save
- Changes are reflected immediately in the HTML

#### Gallery
- Navigate to `/gallery`
- Paste image URL
- Select category (Weddings, New Born, More)
- Add alt text for SEO
- Click "Add Image"

#### Reels
- Navigate to `/reels`
- Paste Instagram post/reel URL
- The system will automatically format it for embedding
- Click "Add Reel"

### Pushing to Git

1. After making changes, click the "Push to Git" button on the dashboard
2. Enter a commit message
3. The system will automatically:
   - Stage all changes
   - Commit with your message
   - Push to the repository

## File Structure

```
backend/
├── app.py                  # Main Flask application
├── html_updater.py         # HTML manipulation utility
├── git_manager.py          # Git operations handler
├── requirements.txt        # Python dependencies
├── data/                   # JSON data storage
│   ├── reviews.json
│   ├── faqs.json
│   ├── gallery.json
│   └── reels.json
├── templates/              # HTML templates
│   ├── dashboard.html
│   ├── reviews.html
│   ├── faqs.html
│   ├── gallery.html
│   └── reels.html
└── static/                 # Static assets (if needed)
```

## API Endpoints

### Reviews
- `GET /api/reviews` - Get all reviews
- `POST /api/reviews` - Add new review
- `PUT /api/reviews/<id>` - Update review
- `DELETE /api/reviews/<id>` - Delete review

### FAQs
- `GET /api/faqs` - Get all FAQs
- `POST /api/faqs` - Add new FAQ
- `PUT /api/faqs/<id>` - Update FAQ
- `DELETE /api/faqs/<id>` - Delete FAQ

### Gallery
- `GET /api/gallery` - Get all images
- `POST /api/gallery` - Add new image
- `PUT /api/gallery/<id>` - Update image
- `DELETE /api/gallery/<id>` - Delete image

### Reels
- `GET /api/reels` - Get all reels
- `POST /api/reels` - Add new reel
- `PUT /api/reels/<id>` - Update reel
- `DELETE /api/reels/<id>` - Delete reel

### Git Operations
- `GET /git/status` - Get git status
- `POST /git/push` - Commit and push changes

## Configuration

### Git Setup

Make sure your repository is initialized and connected to a remote:

```bash
# Initialize git (if not already done)
git init

# Add remote repository
git remote add origin https://github.com/yourusername/your-repo.git

# Configure git credentials
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Security Note

⚠️ **Important**: This is a basic admin panel without authentication. For production use, you should:

1. Add user authentication (Flask-Login or similar)
2. Use environment variables for sensitive data
3. Add HTTPS/SSL certificates
4. Implement rate limiting
5. Add input validation and sanitization
6. Use a production WSGI server (Gunicorn, uWSGI)

## Troubleshooting

### Git Push Fails
- Ensure you have proper git credentials configured
- Check that you have write access to the repository
- Verify the remote URL is correct: `git remote -v`

### HTML Not Updating
- Check file permissions on index.html
- Ensure the path in html_updater.py is correct
- Look for errors in the Flask console

### Dependencies Issues
- Make sure you're using Python 3.8 or higher
- Try upgrading pip: `pip install --upgrade pip`
- Install dependencies one by one if batch install fails

## Future Enhancements

- [ ] User authentication system
- [ ] Image upload functionality (not just URLs)
- [ ] Backup and restore functionality
- [ ] Activity logs
- [ ] Preview changes before saving
- [ ] Scheduled auto-commits
- [ ] Multiple user roles

## Support

For issues or questions, please contact the development team.

## License

This is a custom admin panel built for Shiv's Photography.
