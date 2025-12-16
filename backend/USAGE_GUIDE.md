# 🚀 Complete Usage Guide - Shiv's Photography Backend

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Managing Reviews](#managing-reviews)
3. [Managing FAQs](#managing-faqs)
4. [Managing Gallery](#managing-gallery)
5. [Managing Instagram Reels](#managing-instagram-reels)
6. [Git Integration](#git-integration)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 Quick Start

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in the `backend` folder and run:

```bash
# Navigate to backend folder
cd backend

# Install dependencies
pip install -r requirements.txt
```

Or simply double-click `setup.bat` to install everything automatically.

### Step 2: Start the Server

**Option 1 - Using Command:**
```bash
python app.py
```

**Option 2 - Using Batch File:**
Double-click `start.bat`

### Step 3: Access Admin Panel

Open your web browser and go to:
```
http://localhost:5000
```

You'll see the dashboard with 4 main sections:
- 📝 **Reviews** - Customer testimonials
- ❓ **FAQs** - Frequently Asked Questions
- 🖼️ **Gallery** - Photo gallery management
- 🎬 **Reels** - Instagram reels/videos

---

## 📝 Managing Reviews

### Adding a Review

1. Click on "**Manage Reviews**" from the dashboard
2. Fill in the form:
   - **Customer Name**: Full name (e.g., "Abigail Karsilan")
   - **Initial**: First letter of name (e.g., "A")
   - **Rating**: Select 1-5 stars
   - **Time Ago**: When review was posted (e.g., "3 months ago")
   - **Review Title**: Main quote (e.g., "The photos turned out absolutely beautiful!")
   - **Review Content**: Full review text
   - **Badge** (Optional): Special label (e.g., "Baby Photoshoot Client")

3. Click "**Add Review**"
4. The review will immediately appear on your website!

### Review Display

- First 3 reviews appear in the main review section with large cards
- Additional reviews appear in the "More Customer Reviews" section
- Reviews show Google logo and star ratings automatically

### Deleting a Review

1. Scroll to the review you want to delete
2. Click the red trash icon 🗑️
3. Confirm deletion
4. The website HTML is automatically updated

---

## ❓ Managing FAQs

### Adding an FAQ

1. Click on "**Manage FAQs**" from the dashboard
2. Enter your question and answer:
   - **Question**: The question customers ask (e.g., "Why should we choose you?")
   - **Answer**: Your detailed response

3. Click "**Add FAQ**"

### FAQ Features

- FAQs appear in the "Why Shiv's?" section
- They're displayed with expandable/collapsible format
- Click + icon to expand, - icon to collapse

### Deleting an FAQ

1. Find the FAQ in the list
2. Click the red **Delete** button
3. Confirm deletion

---

## 🖼️ Managing Gallery

### Adding Images

1. Click on "**Manage Gallery**" from the dashboard
2. Fill in the image details:
   - **Image URL**: Direct link to image (e.g., from Pexels, Unsplash, or your own hosting)
   - **Category**: Choose from:
     - Weddings
     - New Born
     - More
   - **Alt Text**: Description for SEO (e.g., "Wedding couple outdoor photography")

3. Click "**Add Image**"

### Where to Get Image URLs

**Option 1 - Stock Photos:**
1. Go to [Pexels](https://www.pexels.com) or [Unsplash](https://unsplash.com)
2. Search for images
3. Right-click on image → "Copy image address"
4. Paste into the URL field

**Option 2 - Your Own Images:**
1. Upload to image hosting service (Imgur, Cloudinary, etc.)
2. Get the direct URL
3. Paste into the URL field

### Gallery Categories

The gallery has filtering buttons:
- **All** - Shows all images
- **Weddings** - Wedding photography
- **New Born** - Baby/newborn photos
- **More** - Other categories

### Deleting Gallery Images

1. Find the image in the grid
2. Click "**Delete**" button
3. Confirm deletion

---

## 🎬 Managing Instagram Reels

### Adding a Reel/Post

1. Click on "**Manage Reels**" from the dashboard
2. Get your Instagram URL:
   
   **Method 1 - From Instagram App:**
   - Open Instagram post/reel
   - Tap the three dots (···)
   - Tap "Link" or "Copy Link"
   - Paste the URL
   
   **Method 2 - From Instagram Web:**
   - Open the post in browser
   - Copy the URL from address bar
   - Example: `https://www.instagram.com/p/ABC123/`

3. Paste the URL in the form
4. Add a title (optional)
5. Click "**Add Reel**"

### Embed Format

The system automatically converts your Instagram URL to the proper embed format:
```
https://www.instagram.com/p/ABC123/
↓
https://www.instagram.com/p/ABC123/embed/
```

### Deleting a Reel

1. Find the reel in the list
2. Click "**Delete**" button
3. Confirm deletion

---

## 🚀 Git Integration

### What is Git Integration?

Every time you make changes (add/delete reviews, FAQs, etc.), the system updates your HTML files. Git integration lets you **automatically push these changes to your GitHub repository**.

### Setting Up Git (First Time Only)

If you haven't set up Git yet:

```bash
# Navigate to your project root (not backend folder)
cd ..

# Initialize git if not already done
git init

# Add your GitHub repository
git remote add origin https://github.com/yourusername/your-repo-name.git

# Configure your identity
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Pushing Changes

**From the Dashboard:**

1. After making changes to reviews/FAQs/gallery/reels
2. Click "**Push to Git**" button (green button in top right)
3. Enter a commit message:
   - Example: "Added new customer reviews"
   - Example: "Updated gallery with wedding photos"
   - Example: "Added 5 new FAQs"
4. Click OK
5. Wait for confirmation

### Checking Git Status

1. Click "**Check Git Status**" button
2. See what files have been changed
3. Review before pushing

### Understanding Commit Messages

Good commit messages help track changes:
- ✅ "Added 3 new reviews from December clients"
- ✅ "Updated gallery with newborn photoshoot images"
- ✅ "Added FAQ about pricing"
- ❌ "Update"
- ❌ "Changes"

---

## 🔧 Troubleshooting

### Server Won't Start

**Problem:** `python app.py` shows an error

**Solutions:**
1. Make sure you're in the `backend` folder
2. Install dependencies: `pip install -r requirements.txt`
3. Check Python version: `python --version` (should be 3.8+)
4. Try: `python -m flask run`

### Can't Access http://localhost:5000

**Problem:** Browser shows "Can't reach this page"

**Solutions:**
1. Make sure the server is running (check terminal/console)
2. Try `http://127.0.0.1:5000` instead
3. Check if port 5000 is available
4. Try different port: `python app.py --port 5001`

### Changes Not Showing on Website

**Problem:** Added content but website looks the same

**Solutions:**
1. Hard refresh browser: `Ctrl + F5` (Windows) or `Cmd + Shift + R` (Mac)
2. Clear browser cache
3. Check if HTML file is being updated (look at file modification time)
4. Check console for errors

### Git Push Fails

**Problem:** "Push to Git" shows an error

**Solutions:**

1. **Authentication Error:**
   ```bash
   # Use GitHub personal access token
   git remote set-url origin https://YOUR_TOKEN@github.com/username/repo.git
   ```

2. **No Remote Set:**
   ```bash
   git remote add origin https://github.com/username/repo.git
   ```

3. **Permission Denied:**
   - Check repository write permissions
   - Verify GitHub credentials
   - Use SSH key authentication

### Images Not Loading in Gallery

**Problem:** Gallery shows broken image icons

**Solutions:**
1. Verify image URL is direct link (ends with .jpg, .png, etc.)
2. Check if image URL is accessible (paste in browser)
3. Use HTTPS URLs, not HTTP
4. Ensure image hosting allows hotlinking

### BeautifulSoup Errors

**Problem:** HTML updater shows parsing errors

**Solutions:**
1. Install/reinstall lxml: `pip install lxml`
2. Check HTML file isn't corrupted
3. Make backup of index.html before testing

---

## 💡 Pro Tips

### 1. Backup Your Data

Before making major changes:
```bash
# Copy your data folder
cp -r backend/data backend/data_backup
```

### 2. Test Before Pushing

1. Make changes in admin panel
2. Preview the website locally
3. If satisfied, push to Git

### 3. Use Descriptive Alt Text

For SEO and accessibility:
- ❌ "img1.jpg"
- ✅ "Bride and groom outdoor wedding ceremony at sunset"

### 4. Organize Gallery by Category

- Keep wedding photos in "Weddings"
- Baby photos in "New Born"
- Use "More" for portraits, events, etc.

### 5. Keep Reviews Authentic

- Use real customer names (with permission)
- Include actual review content
- Add timestamps for credibility

### 6. Regular Backups

Set up automatic git commits:
```bash
# After each session, push to Git
# This creates history of all changes
```

---

## 🆘 Need More Help?

### Common Questions

**Q: Can I undo changes?**
A: Yes! Use Git to revert:
```bash
git log  # See history
git checkout COMMIT_ID -- index.html  # Restore old version
```

**Q: Can multiple people use this?**
A: Currently, no authentication. For multi-user, add Flask-Login.

**Q: Is my data safe?**
A: Data is stored in JSON files. Keep backups and push to Git regularly.

**Q: Can I customize the admin panel?**
A: Yes! Edit HTML templates in `backend/templates/` folder.

### Contact Support

For technical issues:
1. Check error messages in terminal
2. Review this guide
3. Check Flask documentation
4. Contact your developer

---

## 📊 Summary of Workflows

### Daily Workflow
1. Start server (`python app.py`)
2. Open admin panel (http://localhost:5000)
3. Add/edit content
4. Preview changes
5. Push to Git
6. Done!

### Weekly Maintenance
1. Check Git status
2. Review all content
3. Update outdated reviews
4. Add new gallery images
5. Backup data folder

---

**🎉 You're all set! Start managing your website like a pro!**
