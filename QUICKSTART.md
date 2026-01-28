# Quick Start Guide

## 30-Second Setup

### 1. Prepare Credentials (5 minutes)

**Gmail**:
1. Enable 2FA: https://myaccount.google.com/security
2. Create App Password: https://myaccount.google.com/apppasswords
3. Copy the 16-character password

**LinkedIn**: Use your email and password

**Gemini API** (optional):
1. Go to: https://makersuite.google.com/app/apikey
2. Create API Key

### 2. Local Testing (2 minutes)

```bash
# Clone and setup
git clone <repo>
cd Sanchay
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Install Firefox (if needed)
# Ubuntu: sudo apt-get install firefox-geckodriver
# Mac: brew install firefox geckodriver

# Set credentials
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
export LINKEDIN_PASSWORD="your-linkedin-password"
export GEMINI_API_KEY="your-api-key"  # Optional

# Run!
python main.py
```

Check `data/internships.xlsx` for results! 📊

### 3. GitHub Actions Setup (3 minutes)

1. Go to repository **Settings** → **Secrets and variables** → **Actions**
2. Add secrets:
   - `EMAIL_ADDRESS`
   - `EMAIL_PASSWORD`
   - `LINKEDIN_EMAIL`
   - `LINKEDIN_PASSWORD`
   - `GEMINI_API_KEY` (optional)

3. Go to **Actions** tab → **Internship Bot** → **Run workflow**

**Done!** The bot will now run automatically 4 times daily ⏰

## What to Expect

- ✅ Scrapes internships from 4+ sources
- ✅ Saves to `data/internships.xlsx`
- ✅ Sends email with new internships
- ✅ Prevents duplicates automatically
- ✅ Runs on GitHub Actions schedule

## Troubleshooting

**"Login failed"**:
- Use Gmail app password, not main password
- Enable 2FA in Gmail account

**"No internships found"**:
- Check if websites are still accessible
- Review logs in GitHub Actions artifacts

**"Firefox not found"**:
- Ubuntu: `sudo apt-get install firefox-geckodriver`
- Mac: `brew install firefox geckodriver`

## File Structure

```
├── main.py                 # Main script
├── requirements.txt        # Dependencies
├── .github/workflows/      # GitHub Actions
│   └── internship-bot.yml
├── data/
│   └── internships.xlsx    # Results (auto-generated)
├── README.md              # Full documentation
├── CONFIGURATION.md       # Detailed setup guide
└── .gitignore            # Prevents accidental commits
```

## Next Steps

1. ✓ Run locally first: `python main.py`
2. ✓ Check `data/internships.xlsx` for results
3. ✓ Add GitHub Secrets
4. ✓ Monitor GitHub Actions runs
5. ✓ Check your email for notifications!

## Questions?

Refer to:
- **Setup issues**: See [CONFIGURATION.md](CONFIGURATION.md)
- **Features**: See [README.md](README.md)
- **Code details**: Comments in [main.py](main.py)

---

**That's it! You now have an automated internship finder.** 🚀
