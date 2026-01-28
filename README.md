# 🎯 Automated Internship Finder

An intelligent, automated internship discovery bot that scrapes internships from **6+ sources** including major tech company career pages and sends you email notifications with new opportunities. Features Selenium-based LinkedIn scraping, web scraping from Internshala, AngelList, and Glassdoor, major company career pages (Google, Microsoft, Amazon, Meta, Apple, Netflix, Intel, IBM, Oracle, Salesforce), Gmail integration, and optional AI-powered matching using Google's Gemini API.

## 📋 Features

- **Multi-Source Scraping** (6+ Sources)
  - Internshala
  - AngelList
  - Glassdoor
  - **Big Company Career Pages**: Google, Microsoft, Amazon, Meta, Apple, Netflix, Intel, IBM, Oracle, Salesforce
  - LinkedIn (via Selenium with Firefox headless)
  - Gmail job alert emails as fallback

- **Duplicate Prevention**: Automatically tracks and prevents duplicate entries

- **Excel Export**: Stores all internships in a formatted `data/internships.xlsx` file

- **Email Notifications**: Sends formatted email summaries of new internships

- **AI-Powered Enhancement** (Optional): Uses Google Gemini API to score and summarize matches

- **Fully Automated**: GitHub Actions workflow runs 4 times daily automatically

- **Secure**: All credentials via environment variables (no hardcoded secrets)

- **Interactive Skills Input**: Multiple ways to provide your skills and interests

## 🚀 How to Provide Your Skills & Interests

### **Option 1: Interactive Input** (Easiest)
Simply run the script and you'll be prompted:
```bash
python main.py
```
You'll see:
```
======================================================================
🎯 INTERNSHIP FINDER - SKILL INPUT
======================================================================

📝 Enter your skills/interests (or press Enter for defaults):
```

Just type your skills and press Enter:
```
Python, Machine Learning, Data Science
```

### **Option 2: Environment Variable**
Set your skills before running:
```bash
export INTERNSHIP_SEARCH_QUERY="Python, Backend, Cloud Computing"
python main.py
```

Or in GitHub Actions, it automatically uses the environment variable if set.

### **Option 3: Default Skills**
Just press Enter when prompted, and it uses defaults:
```
Python, Data Science, Machine Learning, Backend Development, Full Stack
```

### **Examples of Skills Input**

```
✅ "Python, Data Science, Machine Learning"
✅ "Java, Spring Boot, Backend Development"
✅ "Frontend, React, JavaScript, Web Design"
✅ "Data Analytics, SQL, Python"
✅ "Cloud, AWS, DevOps, Docker"
✅ "Android, Kotlin, Mobile Development"
```

## 📍 Scraping Sources (6+)

### Web-Based Scraping
1. **Internshala** - Popular Indian internship platform
2. **AngelList** - Startup and tech internships
3. **Glassdoor** - Company reviews + internships
4. **Big Company Careers**:
   - 🔵 **Google** (Google Careers)
   - 🟦 **Microsoft** (Microsoft Careers)
   - 🟠 **Amazon** (Amazon Jobs)
   - 📘 **Meta** (Meta Careers)
   - 🍎 **Apple** (Apple Jobs)
   - 🔴 **Netflix** (Netflix Jobs)
   - 🔷 **Intel** (Intel Careers)
   - 🔵 **IBM** (IBM Careers)
   - 🔴 **Oracle** (Oracle Careers)
   - ☁️ **Salesforce** (Salesforce Careers)

### Browser Automation
5. **LinkedIn** (Selenium + Firefox headless) - Real-time job listings

### Email-Based
6. **Gmail Job Alerts** (IMAP) - Fallback from job alert emails

## Setup Instructions

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Sanchay
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export EMAIL_ADDRESS="your-email@gmail.com"
   export EMAIL_PASSWORD="your-gmail-app-password"
   export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
   export LINKEDIN_PASSWORD="your-linkedin-password"
   export GEMINI_API_KEY="your-gemini-api-key"  # Optional
   # Optional: Set custom skills
   export INTERNSHIP_SEARCH_QUERY="Python, Data Science"
   ```

5. **Install additional system dependencies (for Selenium + Firefox)**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install firefox-geckodriver

   # macOS (if needed)
   brew install geckodriver
   ```

6. **Run the script**
   ```bash
   python main.py
   ```
   
   You'll be prompted to enter your skills, or press Enter for defaults.

### GitHub Actions Setup

1. **Create GitHub Secrets**
   - Go to repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `EMAIL_ADDRESS`: Your Gmail address
     - `EMAIL_PASSWORD`: Your Gmail app-specific password
     - `LINKEDIN_EMAIL`: Your LinkedIn email
     - `LINKEDIN_PASSWORD`: Your LinkedIn password
     - `GEMINI_API_KEY`: Your Google Gemini API key (optional)

2. **How to Get Credentials**

   **Gmail Setup**:
   - Enable 2-factor authentication on your Gmail account
   - Create an App Password: https://myaccount.google.com/apppasswords
   - Use the 16-character password as `EMAIL_PASSWORD`

   **LinkedIn Setup**:
   - Use your LinkedIn email and password directly
   - Note: LinkedIn may require additional verification; consider using a dedicated bot account

   **Gemini API Setup** (optional):
   - Visit: https://makersuite.google.com/app/apikey
   - Create a new API key
   - Enable the Generative AI API in your Google Cloud project

3. **Automated Execution**
   - The workflow runs automatically at:
     - 00:00 UTC
     - 06:00 UTC
     - 12:00 UTC
     - 18:00 UTC
   - Manually trigger: Go to Actions tab → "Internship Bot" → "Run workflow"

## 📁 Project Structure

```
Sanchay/
├── main.py                                  # Main script
├── requirements.txt                         # Python dependencies
├── .github/
│   └── workflows/
│       └── internship-bot.yml              # GitHub Actions workflow
├── data/
│   └── internships.xlsx                    # Generated Excel file
├── internship_finder.log                   # Execution logs
└── README.md                                # This file
```

## 🔧 Configuration

### Search Query

You can customize what internships you're looking for in 3 ways:

**Method 1: Interactive** (when running script)
```
python main.py
# Then type your skills when prompted
```

**Method 2: Environment Variable** (before running)
```bash
export INTERNSHIP_SEARCH_QUERY="Your skills here"
python main.py
```

**Method 3: Default** (just press Enter)
```
Uses: "Python, Data Science, Machine Learning, Backend Development, Full Stack"
```

### Email Format

The script sends HTML-formatted emails with a table of new internships including:
- Company name
- Role title
- Location
- Source (where it was found)
- Direct link to apply

## 📊 Data Storage

Internships are stored in `data/internships.xlsx` with the following columns:
- **Company**: Organization name
- **Role**: Position title
- **Location**: Job location
- **Link**: Direct application link
- **Date Found**: When the internship was discovered
- **Source**: Where it was scraped from (Internshala, Glassdoor, Google Careers, etc.)

The Excel file is formatted with:
- Blue header row with white text
- Auto-sized columns for readability
- Automatic appending of new entries

## 🔒 Security Best Practices

1. **Never commit secrets**: All credentials are environment variables only
2. **Use app passwords**: For Gmail, create app-specific passwords instead of using your main password
3. **Dedicated accounts**: Consider using bot accounts for LinkedIn to avoid security flags
4. **Rotate credentials**: Periodically update passwords and API keys
5. **GitHub Secrets**: Never expose secrets in logs or artifacts

## ⚠️ Troubleshooting

### Selenium/Firefox Issues
```bash
# Ensure Firefox is installed
firefox --version

# Ensure GeckoDriver is available
which geckodriver
```

### Gmail Login Failures
- Verify 2FA is enabled on your Gmail account
- Use an app-specific password, not your main password
- Check if Gmail is blocking the login attempt (check security alerts)

### LinkedIn Scraping Not Working
- LinkedIn may require additional verification
- Consider using a dedicated bot account
- Check LinkedIn's Terms of Service for scraping policies

### Email Not Sending
- Verify Gmail credentials are correct
- Check if "Less secure app access" is enabled (if using older Gmail settings)
- Review Gmail activity log for security alerts

### No Internships Found
- Verify search query matches your desired skills
- Check if websites have changed their HTML structure
- Review logs in `internship_finder.log`
- Big company career pages may require JavaScript rendering (currently limited)

## 📝 Logs

Execution logs are stored in `internship_finder.log` with timestamps and log levels:
- **INFO**: General progress updates
- **WARNING**: Non-critical issues
- **ERROR**: Critical errors

## 🤖 Gemini API Enhancement

When `GEMINI_API_KEY` is provided, the script uses Google's Gemini model to:
1. Score each internship (0-100) based on skill match
2. Provide reasoning for the score
3. Enhance email notifications with match analysis

This is optional and the script works perfectly fine without it.

## 📧 Email Customization

To modify email template, edit the `send_email_notification()` function in `main.py`:
- Change HTML styling
- Add additional fields
- Modify subject line

## ⏱️ Execution Time

- Local execution: 5-10 minutes depending on network
- GitHub Actions: Typically completes in 10-15 minutes

## 🤝 Contributing

Feel free to extend the bot:
- Add more scraping sources
- Improve parsing logic
- Add filters for specific roles/locations
- Integrate with other job platforms

## 📜 License

This project is open source and available under the MIT License.

## ⚡ Tips

1. **Test locally first**: Run `python main.py` locally before relying on GitHub Actions
2. **Monitor artifacts**: Check GitHub Actions artifacts to verify Excel file generation
3. **Review logs**: Always check execution logs for parsing or connection issues
4. **Adjust schedule**: Modify cron times in the workflow if you prefer different notification times
5. **Filter manually**: Use Excel filters to sort internships by company, location, or source
6. **Customize skills**: Different searches will yield different results - experiment!

## 🆘 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review execution logs in GitHub Actions artifacts
3. Ensure all environment variables are correctly set
4. Test web scraping sources independently to verify they're still accessible

---

**Happy internship hunting! 🎉**

## 🚀 Setup Instructions

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Sanchay
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   export EMAIL_ADDRESS="your-email@gmail.com"
   export EMAIL_PASSWORD="your-gmail-app-password"
   export LINKEDIN_EMAIL="your-linkedin-email@gmail.com"
   export LINKEDIN_PASSWORD="your-linkedin-password"
   export GEMINI_API_KEY="your-gemini-api-key"  # Optional
   export INTERNSHIP_SEARCH_QUERY="Python, Data Science, Machine Learning"  # Optional
   ```

5. **Install additional system dependencies (for Selenium + Firefox)**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install firefox-geckodriver

   # macOS (if needed)
   brew install geckodriver
   ```

6. **Run the script**
   ```bash
   python main.py
   ```

### GitHub Actions Setup

1. **Create GitHub Secrets**
   - Go to repository → Settings → Secrets and variables → Actions
   - Add the following secrets:
     - `EMAIL_ADDRESS`: Your Gmail address
     - `EMAIL_PASSWORD`: Your Gmail app-specific password
     - `LINKEDIN_EMAIL`: Your LinkedIn email
     - `LINKEDIN_PASSWORD`: Your LinkedIn password
     - `GEMINI_API_KEY`: Your Google Gemini API key (optional)

2. **How to Get Credentials**

   **Gmail Setup**:
   - Enable 2-factor authentication on your Gmail account
   - Create an App Password: https://myaccount.google.com/apppasswords
   - Use the 16-character password as `EMAIL_PASSWORD`

   **LinkedIn Setup**:
   - Use your LinkedIn email and password directly
   - Note: LinkedIn may require additional verification; consider using a dedicated bot account

   **Gemini API Setup** (optional):
   - Visit: https://makersuite.google.com/app/apikey
   - Create a new API key
   - Enable the Generative AI API in your Google Cloud project

3. **Automated Execution**
   - The workflow runs automatically at:
     - 00:00 UTC
     - 06:00 UTC
     - 12:00 UTC
     - 18:00 UTC
   - Manually trigger: Go to Actions tab → "Internship Bot" → "Run workflow"

## 📁 Project Structure

```
Sanchay/
├── main.py                                  # Main script
├── requirements.txt                         # Python dependencies
├── .github/
│   └── workflows/
│       └── internship-bot.yml              # GitHub Actions workflow
├── data/
│   └── internships.xlsx                    # Generated Excel file
├── internship_finder.log                   # Execution logs
└── README.md                                # This file
```

## 🔧 Configuration

### Search Query

By default, the script uses: `"Python, Data Science, Machine Learning, Backend Development"`

To customize:
```bash
export INTERNSHIP_SEARCH_QUERY="Your skills here"
python main.py
```

Or provide input when prompted.

### Email Format

The script sends HTML-formatted emails with a table of new internships including:
- Company name
- Role title
- Location
- Source (where it was found)
- Direct link to apply

## 📊 Data Storage

Internships are stored in `data/internships.xlsx` with the following columns:
- **Company**: Organization name
- **Role**: Position title
- **Location**: Job location
- **Link**: Direct application link
- **Date Found**: When the internship was discovered
- **Source**: Where it was scraped from

The Excel file is formatted with:
- Blue header row with white text
- Auto-sized columns for readability
- Automatic appending of new entries

## 🔒 Security Best Practices

1. **Never commit secrets**: All credentials are environment variables only
2. **Use app passwords**: For Gmail, create app-specific passwords instead of using your main password
3. **Dedicated accounts**: Consider using bot accounts for LinkedIn to avoid security flags
4. **Rotate credentials**: Periodically update passwords and API keys
5. **GitHub Secrets**: Never expose secrets in logs or artifacts

## ⚠️ Troubleshooting

### Selenium/Firefox Issues
```bash
# Ensure Firefox is installed
firefox --version

# Ensure GeckoDriver is available
which geckodriver
```

### Gmail Login Failures
- Verify 2FA is enabled on your Gmail account
- Use an app-specific password, not your main password
- Check if Gmail is blocking the login attempt (check security alerts)

### LinkedIn Scraping Not Working
- LinkedIn may require additional verification
- Consider using a dedicated bot account
- Check LinkedIn's Terms of Service for scraping policies

### Email Not Sending
- Verify Gmail credentials are correct
- Check if "Less secure app access" is enabled (if using older Gmail settings)
- Review Gmail activity log for security alerts

### No Internships Found
- Verify search query matches your desired skills
- Check if websites have changed their HTML structure
- Review logs in `internship_finder.log`

## 📝 Logs

Execution logs are stored in `internship_finder.log` with timestamps and log levels:
- **INFO**: General progress updates
- **WARNING**: Non-critical issues
- **ERROR**: Critical errors

## 🤖 Gemini API Enhancement

When `GEMINI_API_KEY` is provided, the script uses Google's Gemini model to:
1. Score each internship (0-100) based on skill match
2. Provide reasoning for the score
3. Enhance email notifications with match analysis

This is optional and the script works perfectly fine without it.

## 📧 Email Customization

To modify email template, edit the `send_email_notification()` function in `main.py`:
- Change HTML styling
- Add additional fields
- Modify subject line

## ⏱️ Execution Time

- Local execution: 2-5 minutes depending on network
- GitHub Actions: Typically completes in 5-10 minutes

## 🤝 Contributing

Feel free to extend the bot:
- Add more scraping sources
- Improve parsing logic
- Add filters for specific roles/locations
- Integrate with other job platforms

## 📜 License

This project is open source and available under the MIT License.

## ⚡ Tips

1. **Test locally first**: Run `python main.py` locally before relying on GitHub Actions
2. **Monitor artifacts**: Check GitHub Actions artifacts to verify Excel file generation
3. **Review logs**: Always check execution logs for parsing or connection issues
4. **Adjust schedule**: Modify cron times in the workflow if you prefer different notification times
5. **Filter manually**: Use Excel filters to sort internships by company, location, or source

## 🆘 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review execution logs in GitHub Actions artifacts
3. Ensure all environment variables are correctly set
4. Test web scraping sources independently to verify they're still accessible

---

**Happy internship hunting! 🎉**
