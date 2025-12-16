# ⚡ Quick Reference Card

## 🚀 Getting Started

### First Time Setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Open: http://localhost:5000

### Daily Use
Double-click: `start.bat`
Open: http://localhost:5000

---

## 📝 Common Tasks

### Add Review
1. Dashboard → Manage Reviews
2. Fill: Name, Initial, Rating, Title, Content
3. Click: Add Review
4. Done! ✅

### Add Gallery Image
1. Dashboard → Manage Gallery
2. Paste: Image URL
3. Select: Category (Weddings/Newborn/More)
4. Add: Alt text
5. Click: Add Image
6. Done! ✅

### Add FAQ
1. Dashboard → Manage FAQs
2. Enter: Question and Answer
3. Click: Add FAQ
4. Done! ✅

### Add Instagram Reel
1. Dashboard → Manage Reels
2. Copy Instagram URL from post
3. Paste URL
4. Click: Add Reel
5. Done! ✅

### Push to GitHub
1. Click: "Push to Git" (green button)
2. Enter: Commit message
3. Click: OK
4. Wait for success message
5. Done! ✅

---

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| Server won't start | `pip install -r requirements.txt` |
| Can't access localhost:5000 | Check if server is running |
| Changes not showing | Hard refresh: `Ctrl + F5` |
| Git push fails | Check git credentials |
| Image not loading | Verify direct image URL |

---

## 📁 File Locations

```
backend/
├── app.py              ← Main application
├── data/               ← All content stored here
│   ├── reviews.json
│   ├── faqs.json
│   ├── gallery.json
│   └── reels.json
└── templates/          ← Admin pages
```

---

## 🎯 URLs

| Page | URL |
|------|-----|
| Dashboard | http://localhost:5000 |
| Reviews | http://localhost:5000/reviews |
| FAQs | http://localhost:5000/faqs |
| Gallery | http://localhost:5000/gallery |
| Reels | http://localhost:5000/reels |

---

## 💡 Pro Tips

✅ **Always backup before major changes**
```bash
cp -r data data_backup
```

✅ **Test locally before pushing**
- Make changes
- View website
- If good → Push to Git

✅ **Use descriptive commit messages**
- Good: "Added 5 wedding photos to gallery"
- Bad: "Update"

✅ **Keep URLs organized**
- Use image hosting (Imgur, Cloudinary)
- Keep URLs in a spreadsheet

✅ **Regular maintenance**
- Weekly: Check all content
- Monthly: Backup data folder
- Always: Push to Git after changes

---

## 🔑 Keyboard Shortcuts

| Action | Windows | Mac |
|--------|---------|-----|
| Hard Refresh | Ctrl + F5 | Cmd + Shift + R |
| New Tab | Ctrl + T | Cmd + T |
| Dev Tools | F12 | Cmd + Option + I |

---

## 📞 Emergency Contacts

**Issue**: Data lost
**Solution**: Restore from Git
```bash
git log
git checkout COMMIT_ID -- backend/data/
```

**Issue**: HTML corrupted
**Solution**: Restore from Git
```bash
git checkout HEAD -- index.html
```

**Issue**: Everything broken
**Solution**: Full restore
```bash
git reset --hard HEAD
```

---

## ✅ Daily Checklist

- [ ] Start server
- [ ] Check dashboard loads
- [ ] Add/update content
- [ ] Preview changes
- [ ] Push to Git
- [ ] Verify live site

---

**Print this card for quick reference! 📋**
