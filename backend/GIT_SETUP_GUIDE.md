# 🔧 Git Setup & Troubleshooting

## ⚠️ Error: "Git command failed"

This error appears when Git is not properly configured. Here's how to fix it:

---

## ✅ Quick Fix (Recommended)

### Step 1: Run the Git Setup Helper

Open PowerShell in the `backend` folder and run:

```bash
python setup_git.py
```

This interactive script will:
- ✅ Check if Git is installed
- ✅ Initialize the repository
- ✅ Configure your name and email
- ✅ Set up remote repository (GitHub)
- ✅ Create initial commit

Just follow the prompts!

---

## 🛠️ Manual Setup (Alternative)

If you prefer to set up Git manually:

### Step 1: Check if Git is Installed

```bash
git --version
```

If you see a version number, Git is installed ✓

If not, download from: https://git-scm.com/downloads

### Step 2: Navigate to Your Project

```bash
cd "c:\Users\Ahamed Shafeek\Downloads\shivsphotography-main\shivsphotography-main"
```

### Step 3: Initialize Git Repository

```bash
git init
```

### Step 4: Configure Your Identity

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 5: Add GitHub Remote

Replace with your actual GitHub repository URL:

```bash
git remote add origin https://github.com/AhamedShafeek/shivswebsite.git
```

**Note:** Get your repository URL from GitHub:
1. Go to your repository on GitHub
2. Click the green "Code" button
3. Copy the HTTPS URL

### Step 6: Create .gitignore (Optional)

Create a file named `.gitignore` in your project root with:

```
__pycache__/
*.pyc
.env
venv/
node_modules/
```

### Step 7: Make Initial Commit

```bash
git add .
git commit -m "Initial commit with backend system"
```

### Step 8: Push to GitHub (First Time)

```bash
git branch -M main
git push -u origin main
```

---

## 🎯 After Setup

Once Git is configured, the admin panel features will work:

1. ✅ **Check Git Status** - View uncommitted changes
2. ✅ **Push to Git** - Upload changes to GitHub
3. ✅ All changes automatically tracked

---

## 🔍 Verify Setup

Test if Git is working:

```bash
# Check git status
git status

# Check remote
git remote -v

# Check your config
git config user.name
git config user.email
```

You should see output for all commands ✓

---

## 🆘 Common Issues

### Issue: "Git is not recognized"
**Fix:** Install Git from https://git-scm.com/downloads

### Issue: "Remote origin already exists"
**Fix:** Update the URL:
```bash
git remote set-url origin https://github.com/username/repo.git
```

### Issue: "Permission denied (publickey)"
**Fix:** Use HTTPS instead of SSH, or set up SSH keys

### Issue: "Failed to push"
**Fix:** Pull first:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

---

## 📱 GitHub Personal Access Token (If Needed)

If GitHub asks for a password:

1. Go to GitHub.com → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. Select scopes: `repo` (all)
5. Copy the token
6. Use token as password when pushing

Or update your remote URL with token:
```bash
git remote set-url origin https://YOUR_TOKEN@github.com/username/repo.git
```

---

## ✅ Success Checklist

- [ ] Git is installed
- [ ] Repository is initialized (`git init`)
- [ ] User name and email configured
- [ ] Remote repository added
- [ ] Initial commit made
- [ ] Successfully pushed to GitHub
- [ ] Admin panel "Push to Git" works!

---

## 🎉 Once Setup is Complete

Your admin panel will be fully functional:

1. Make changes (add reviews, gallery, etc.)
2. Click "Push to Git"
3. Enter commit message
4. Changes automatically uploaded to GitHub!

---

## 🆘 Still Having Issues?

Try the automated setup:
```bash
python setup_git.py
```

This will guide you through each step interactively!
