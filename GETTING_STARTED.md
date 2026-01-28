# 🚀 Getting Started - Automated Internship Finder

Welcome! This guide will get you from zero to fully operational in under 10 minutes.

## What You're Getting

An **automated bot** that:
- 🔍 Scrapes internships from **6+ sources** daily including major tech companies
- 📧 Sends you email notifications
- 💾 Stores everything in Excel
- 🤖 Uses AI to match internships to your skills (optional)
- ⏰ Runs automatically 4 times daily on GitHub
- 📍 Focuses on big companies: Google, Microsoft, Amazon, Meta, Apple, Netflix, Intel, IBM, Oracle, Salesforce

## 📝 Where & How to Input Your Skills

You have **3 easy options**:

### **Option 1: Interactive (Easiest - Just type!)**
```bash
python main.py
```
You'll see a prompt:
```
======================================================================
🎯 INTERNSHIP FINDER - SKILL INPUT
======================================================================

📝 Enter your skills/interests (or press Enter for defaults):
```
Just type what you're looking for:
```
Python, Machine Learning, Data Science
```
Or press Enter to use defaults.

### **Option 2: Environment Variable (Before running)**
```bash
export INTERNSHIP_SEARCH_QUERY="Python, Backend Development"
python main.py
```

### **Option 3: Use Defaults (Just press Enter)**
```
Default: "Python, Data Science, Machine Learning, Backend Development, Full Stack"
```

### Example Skills You Can Enter:
```
✅ "Python, Data Science, Machine Learning"
✅ "Java, Spring Boot, Backend"
✅ "Frontend, React, JavaScript, Web Design"
✅ "Data Analytics, SQL, Python"
✅ "Cloud, AWS, DevOps, Docker"
✅ "Android, Mobile Development"
✅ "Cybersecurity, Network Security"
✅ "Product Management, Data Analysis"
```

---

## Choose Your Path

### 🟢 Fast Track (If you trust the setup)
**Time: 3 minutes**

1. **Prepare credentials** (see credentials section below)
2. **Add GitHub Secrets** (Settings → Secrets and variables → Actions)
3. **Done!** Workflow runs automatically 4x daily

### 🟡 Standard Track (Recommended - Test locally first)
**Time: 10 minutes**

1. **Prepare credentials**
2. **Setup locally** (clone, venv, install)
3. **Run test** (python test_setup.py)
4. **Test script** (python main.py) - **Enter your skills when prompted!**
5. **Check results** (data/internships.xlsx)
6. **Deploy to GitHub** (add secrets, push)

### 🔴 Deep Dive (If you want to understand everything)
**Time: 30 minutes**

1. Read **README.md** - Complete feature overview
2. Read **CONFIGURATION.md** - Detailed setup
3. Review **main.py** - Understand the code
4. Run **test_setup.py** - Validate setup
5. Execute **main.py** - **Enter your skills!** See it in action
6. Deploy to **GitHub Actions**

---

## 🔑 Preparing Your Credentials (5 minutes)

### Gmail (EMAIL_ADDRESS & EMAIL_PASSWORD)

1. Go to https://myaccount.google.com
2. Click **Security** (left sidebar)
3. Turn on **2-Step Verification** (if not already on)
4. Find **App passwords** section
5. Generate a password for "Mail" and "Computer"
6. Copy the 16-character password

**Now you have**:
```
EMAIL_ADDRESS = your-email@gmail.com
EMAIL_PASSWORD = 16-character-app-password
```

⚠️ **NOT your Gmail password, the app password!**

### LinkedIn (LINKEDIN_EMAIL & LINKEDIN_PASSWORD)

Just use your LinkedIn credentials:
```
LINKEDIN_EMAIL = your-linkedin-email@gmail.com
LINKEDIN_PASSWORD = your-linkedin-password
```

### Gemini API (Optional - for AI matching)

1. Go to https://makersuite.google.com/app/apikey
2. Click **Create API Key**
3. Copy it

```
GEMINI_API_KEY = your-gemini-api-key
```

---

## 📍 Scraping Sources You'll Access

**6+ Job Sources**:
- ✅ Internshala
- ✅ AngelList
- ✅ Glassdoor
- ✅ **Google Careers**
- ✅ **Microsoft Careers**
- ✅ **Amazon Jobs**
- ✅ **Meta Careers**
- ✅ **Apple Jobs**
- ✅ **Netflix Jobs**
- ✅ **Intel Careers**
- ✅ **IBM Careers**
- ✅ **Oracle Careers**
- ✅ **Salesforce Careers**
- ✅ LinkedIn (Browser automation)
- ✅ Gmail Job Alerts (IMAP)

---

## 📥 Local Setup (Choose One)

### Option A: Using Command Line

```bash
# 1. Clone repository
git clone <your-repo-url>
cd Sanchay

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Firefox (if needed)
# Ubuntu/Debian:
sudo apt-get install firefox-geckodriver

# Mac:
brew install firefox geckodriver

# 5. Set environment variables
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
export LINKEDIN_PASSWORD="your-linkedin-password"
export GEMINI_API_KEY="your-api-key"  # Optional

# 6. Test environment
python test_setup.py

# 7. Run the script!
python main.py
```

### Option B: Step by Step in Python

```python
# Create and activate venv
python3 -m venv venv
source venv/bin/activate

# Install packages
import subprocess
subprocess.run(["pip", "install", "-r", "requirements.txt"])

# Set credentials (in your terminal, not in Python)
# export EMAIL_ADDRESS="..."
# export EMAIL_PASSWORD="..."
# etc.

# Then run
python main.py
```

---

## ✅ After Local Testing

If everything works locally:

1. **The script will prompt you for skills**:
   ```
   📝 Enter your skills/interests (or press Enter for defaults):
   ```
   
2. **You enter your skills**, for example:
   ```
   Python, Machine Learning, Data Science
   ```

3. **Check the results**:
   - Look at `data/internships.xlsx` ✓
   - Check email for notification ✓
   - Review `internship_finder.log` ✓

4. **If all good, deploy to GitHub**

---

## 🚀 GitHub Actions Deployment (3 minutes)

### Step 1: Add Secrets

1. Go to your GitHub repository
2. Click **Settings** at the top
3. Click **Secrets and variables** → **Actions** (left sidebar)
4. Click **New repository secret** and add:

| Secret Name | Value |
|------------|-------|
| EMAIL_ADDRESS | your-email@gmail.com |
| EMAIL_PASSWORD | your-app-password |
| LINKEDIN_EMAIL | your-linkedin-email |
| LINKEDIN_PASSWORD | your-linkedin-password |
| GEMINI_API_KEY | your-api-key (optional) |

### Step 2: Test Manually

1. Go to **Actions** tab
2. Click **Internship Bot** workflow
3. Click **Run workflow**
4. Wait 10 minutes for it to complete
5. Download artifact to verify it worked

### Step 3: Automatic Execution

The workflow now runs automatically:
- **00:00 UTC** (midnight)
- **06:00 UTC** (6 AM)
- **12:00 UTC** (noon)
- **18:00 UTC** (6 PM)

You'll get email notifications with new internships! 📧

---

## 📊 What to Expect

### First Run Output

```
data/internships.xlsx:
├─ Column A: Company
├─ Column B: Role
├─ Column C: Location
├─ Column D: Link (clickable)
├─ Column E: Date Found
└─ Column F: Source (Glassdoor, Google Careers, LinkedIn, etc.)
```

### Email Notification

You'll receive an HTML email like:

```
Subject: [Internship Bot] Found 25 New Internships

Company       | Role              | Location    | Source
--------------|-------------------|-------------|----------
Google        | Software Intern   | Mountain View | Google Careers
Microsoft     | SDE Intern        | Seattle     | Microsoft Careers
Amazon        | ML Intern         | Remote      | Amazon Jobs
Meta          | Data Eng Intern   | Menlo Park  | Meta Careers
Glassdoor Co. | PM Intern         | NYC         | Glassdoor
...
```

---

## 🆘 Troubleshooting

### "Gmail login failed"

❌ **Wrong**: Using your regular Gmail password  
✅ **Right**: Using the 16-character app password from Gmail

Go back to https://myaccount.google.com/apppasswords

### "No internships found"

This is normal if:
- Running first time (takes time to scrape)
- Websites changed structure (need selector updates)
- No new internships matching your search

Check the log file and review script output.

### "Firefox not found"

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install firefox-geckodriver
```

**Mac**:
```bash
brew install firefox geckodriver
```

### "Module not found"

```bash
pip install -r requirements.txt
```

### "I don't know what skills to enter"

Enter what interests you! Examples:
```
✅ "Python, Backend, Web Development"
✅ "Data Science, Machine Learning, Analytics"
✅ "Frontend, React, JavaScript"
✅ "DevOps, Cloud, AWS, Docker"
✅ "Mobile, Android, Kotlin"
```

Or just press Enter to use defaults and let the bot find opportunities!

---

## 📖 Full Documentation

| Document | Purpose |
|----------|---------|
| **README.md** | Complete feature guide |
| **QUICKSTART.md** | 5-minute version of this |
| **CONFIGURATION.md** | Detailed credential setup |
| **FILE_STRUCTURE.md** | Project organization |
| **PROJECT_SUMMARY.md** | Technical overview |
| **main.py** | Well-commented source code |

---

## 🎯 Next Steps

### After Setup Works

1. **Customize search query** (optional):
   ```bash
   export INTERNSHIP_SEARCH_QUERY="Data Science, Machine Learning"
   python main.py
   ```
   Or just enter it when prompted!

2. **Check logs regularly**:
   ```bash
   tail -f internship_finder.log
   ```

3. **Monitor GitHub Actions**:
   - Go to Actions tab
   - Check run history
   - Download artifacts

4. **Verify Excel file**:
   - Check for duplicates
   - Apply filters
   - Sort by source/date

---

## ⚡ Pro Tips

1. **Test locally first** before relying on GitHub Actions
2. **Check your spam folder** for email notifications
3. **Use Excel filters** to sort internships
4. **Try different search queries** to find more opportunities
5. **Monitor runs** in GitHub Actions for errors

---

## 🔒 Security Reminders

✅ **Do**:
- Use app passwords (not main password)
- Store credentials in GitHub Secrets
- Keep `.env` out of git
- Rotate passwords regularly

❌ **Don't**:
- Commit credentials to git
- Use main Gmail password
- Hardcode secrets in code
- Share GitHub Secrets

---

## 📞 Quick Support

**Question**: Where do I enter my skills?  
**Answer**: When you run `python main.py`, it will prompt you!

**Question**: It's not sending emails!  
**Answer**: Check that EMAIL_ADDRESS is correct and 2FA is on

**Question**: Nothing is being scraped!  
**Answer**: Run `python test_setup.py` to verify setup

**Question**: How often does it run?  
**Answer**: 4 times daily (00:00, 06:00, 12:00, 18:00 UTC)

**Question**: Can I run it manually?  
**Answer**: Yes! Go to Actions → Internship Bot → Run workflow

---

## 🎉 You're All Set!

You now have a fully automated internship finder that:
- ✅ Scrapes 6+ sources including big companies
- ✅ Sends email notifications
- ✅ Stores results in Excel
- ✅ Prevents duplicates
- ✅ Uses AI for matching (optional)
- ✅ Runs automatically on GitHub

**Happy internship hunting!** 🚀

---

### Questions?

1. Check the relevant documentation file
2. Review the comments in main.py
3. Check execution logs
4. Run test_setup.py for diagnostics

**Last Updated**: January 2026  
**Status**: Production Ready ✅
