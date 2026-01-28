# Configuration Guide for Automated Internship Finder

## Environment Variables Setup

All credentials are passed as environment variables. Do NOT use a `.env` file as it could accidentally be committed to git.

### Required Credentials

#### 1. Gmail Setup (EMAIL_ADDRESS & EMAIL_PASSWORD)

**Why needed**: 
- Send email notifications of new internships
- Read unread job alert emails as fallback source
- Authenticate with IMAP and SMTP protocols

**Setup steps**:

1. Go to https://myaccount.google.com
2. Navigate to **Security** (left sidebar)
3. Enable **2-Step Verification** if not already enabled
4. Create an **App Password**:
   - After 2FA is enabled, scroll down to "App passwords"
   - Select "Mail" and "Windows Computer" (or your device)
   - Generate a 16-character password
5. Copy this password as your `EMAIL_PASSWORD`

**Environment variable**:
```bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="16-character-app-password"
```

**Test**:
```python
import smtplib
from email.mime.text import MIMEText

email = "your-email@gmail.com"
password = "your-app-password"

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email, password)
        print("✓ Gmail SMTP authentication successful")
except Exception as e:
    print(f"✗ Failed: {e}")
```

#### 2. LinkedIn Credentials (LINKEDIN_EMAIL & LINKEDIN_PASSWORD)

**Why needed**:
- Authenticate with LinkedIn
- Scrape job listings using Selenium in headless mode
- Search for specific internship roles

**Setup**:

1. Use your actual LinkedIn email and password
2. Consider creating a dedicated bot account to avoid security locks
3. LinkedIn may trigger 2FA during automation; have verification codes ready

**Environment variable**:
```bash
export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
export LINKEDIN_PASSWORD="your-linkedin-password"
```

⚠️ **Note**: LinkedIn's Terms of Service restrict automated scraping. Use responsibly and consider:
- Adding delays between requests
- Not storing/selling scraped data
- Respecting LinkedIn's robots.txt

#### 3. Gemini API Key (Optional)

**Why needed**:
- AI-powered matching of internships to your skills
- Score internships based on relevance (0-100)
- Provide reasoning for match scores

**Setup**:

1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click "Create API Key"
4. Enable the Generative AI API in your Google Cloud project if prompted
5. Copy the API key

**Environment variable**:
```bash
export GEMINI_API_KEY="your-gemini-api-key"
```

**Test**:
```python
import google.generativeai as genai

genai.configure(api_key="your-key")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Hello")
print("✓ Gemini API working")
```

#### 4. Search Query (Optional)

**Why needed**:
- Customize internship search to your skills/interests
- Default: "Python, Data Science, Machine Learning, Backend Development"

**Environment variable**:
```bash
export INTERNSHIP_SEARCH_QUERY="Python, Machine Learning, Data Science"
```

## Local Development Setup

### Step 1: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 2: Set Environment Variables

**Option A: Using export commands (temporary)**
```bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
export LINKEDIN_PASSWORD="your-linkedin-password"
export GEMINI_API_KEY="your-gemini-api-key"
```

**Option B: Using a temporary shell script (not committed to git)**

Create `setup_env.sh` (NOT committed to git):
```bash
#!/bin/bash
export EMAIL_ADDRESS="your-email@gmail.com"
export EMAIL_PASSWORD="your-app-password"
export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
export LINKEDIN_PASSWORD="your-linkedin-password"
export GEMINI_API_KEY="your-gemini-api-key"
```

Then source it:
```bash
source setup_env.sh
```

### Step 3: Install Firefox & GeckoDriver

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install firefox-geckodriver
```

**macOS**:
```bash
brew install firefox geckodriver
```

**Manual installation**:
1. Download Firefox from https://www.mozilla.org/firefox/
2. Download GeckoDriver from https://github.com/mozilla/geckodriver/releases
3. Add GeckoDriver to PATH

### Step 4: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the Script
```bash
python main.py
```

## GitHub Actions Setup

### Step 1: Add GitHub Secrets

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** for each:

| Secret Name | Value |
|------------|-------|
| EMAIL_ADDRESS | your-email@gmail.com |
| EMAIL_PASSWORD | your-gmail-app-password |
| LINKEDIN_EMAIL | your-linkedin-email |
| LINKEDIN_PASSWORD | your-linkedin-password |
| GEMINI_API_KEY | your-gemini-api-key (optional) |

### Step 2: Verify Workflow

1. Go to **Actions** tab in your repository
2. Select **Internship Bot** workflow
3. Click **Run workflow** to test manually
4. Check the workflow run logs

### Step 3: Scheduled Runs

The workflow is configured to run at:
- **00:00 UTC** (12:00 AM)
- **06:00 UTC** (6:00 AM)
- **12:00 UTC** (12:00 PM)
- **18:00 UTC** (6:00 PM)

Adjust the cron expressions in `.github/workflows/internship-bot.yml` if needed:
```yaml
schedule:
  - cron: '0 0 * * *'   # Edit these times
  - cron: '0 6 * * *'
  - cron: '0 12 * * *'
  - cron: '0 18 * * *'
```

[Cron format reference](https://crontab.guru/)

## Troubleshooting Credentials

### Gmail Issues

**Problem**: "Login failed" or "Invalid credentials"
- ✓ Ensure you're using an **app password**, not your main Gmail password
- ✓ Verify 2-factor authentication is enabled
- ✓ Check https://myaccount.google.com/security-checkup
- ✓ Allow access from "less secure apps" if using older Gmail

**Problem**: Connection timeout
- ✓ Check your firewall/proxy settings
- ✓ Verify IMAP is enabled in Gmail: https://myaccount.google.com/lesssecureapps

### LinkedIn Issues

**Problem**: "Selenium timeout" or "Element not found"
- ✓ LinkedIn page structure may have changed; update selectors in `main.py`
- ✓ Add longer wait times in Selenium script
- ✓ Try with a fresh LinkedIn account

**Problem**: "Account locked" or "Verification required"
- ✓ LinkedIn detected unusual activity
- ✓ Sign in manually to verify account
- ✓ Consider using a dedicated bot account
- ✓ Add longer delays between requests

### Gemini API Issues

**Problem**: "Invalid API key"
- ✓ Verify key from https://makersuite.google.com/app/apikey
- ✓ Ensure the Generative AI API is enabled in Google Cloud

**Problem**: "Quota exceeded"
- ✓ Check your API usage limits
- ✓ The script limits Gemini calls to 5 internships per run
- ✓ Upgrade your API tier if needed

## Testing Your Configuration

### Test Email Credentials
```python
import smtplib
import imapclient

# SMTP (sending)
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your-email@gmail.com", "your-app-password")
    print("✓ SMTP works")
except Exception as e:
    print(f"✗ SMTP failed: {e}")

# IMAP (reading)
try:
    server = imapclient.IMAPClient("imap.gmail.com", ssl=True)
    server.login("your-email@gmail.com", "your-app-password")
    server.select_folder("INBOX")
    print("✓ IMAP works")
except Exception as e:
    print(f"✗ IMAP failed: {e}")
```

### Test LinkedIn Selenium
```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
driver.get("https://www.linkedin.com")
print(f"✓ Selenium works - Title: {driver.title}")
driver.quit()
```

### Test Gemini API
```python
import google.generativeai as genai

genai.configure(api_key="your-key")
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Test")
print(f"✓ Gemini works - Response: {response.text[:50]}")
```

## Security Best Practices

1. **Never commit credentials**: Verify `.gitignore` prevents this
2. **Use app passwords**: Don't use your main Gmail password
3. **Rotate regularly**: Change passwords/keys every 90 days
4. **Audit GitHub Secrets**: Regularly review who has access
5. **Monitor activity**: Check Gmail and LinkedIn security logs
6. **Clean up logs**: GitHub Actions artifacts are retained for 30 days

## Common Configuration Mistakes

❌ **Wrong**: Hardcoding credentials in `main.py`
✓ **Right**: Using `os.getenv("SECRET_NAME")`

❌ **Wrong**: Using main Gmail password
✓ **Right**: Using app-specific password from Gmail account

❌ **Wrong**: Committing `.env` file
✓ **Right**: Using GitHub Secrets for Actions, environment variables locally

❌ **Wrong**: Using LinkedIn password in plain text
✓ **Right**: Storing in GitHub Secrets

## Next Steps

1. Configure all required credentials
2. Test locally with `python main.py`
3. Verify Excel file generation in `data/internships.xlsx`
4. Add GitHub Secrets
5. Test GitHub Actions workflow with manual trigger
6. Let it run automatically 4 times daily!

---

For questions or issues, refer to the main README.md or review execution logs.
