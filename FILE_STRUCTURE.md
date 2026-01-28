# Project File Structure & Overview

## Directory Structure

```
Sanchay/
│
├── 📄 main.py                          # Main automation script (700+ lines)
├── 📄 requirements.txt                 # Python dependencies (7 packages)
├── 📄 test_setup.py                    # Environment validation script
├── 📄 .gitignore                       # Prevents credential commits
│
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 internship-bot.yml       # GitHub Actions workflow
│
├── 📁 data/                            # Output directory (auto-created)
│   └── 📄 internships.xlsx             # Results (auto-generated)
│
├── 📚 Documentation/
│   ├── 📄 README.md                    # Complete documentation
│   ├── 📄 QUICKSTART.md               # 5-minute setup guide
│   ├── 📄 CONFIGURATION.md            # Detailed setup instructions
│   ├── 📄 PROJECT_SUMMARY.md          # This overview
│   └── 📄 internship_finder.log       # Execution logs (auto-generated)
│
└── 📁 .git/                            # Git repository
```

## File Descriptions

### Core Application Files

#### main.py (700+ lines)
Complete internship finder script with:
- **Scraping functions** (4 sources)
- **Data management** (Excel read/write)
- **Email notifications** (HTML formatted)
- **Gemini API integration** (optional AI)
- **Error handling** (comprehensive)
- **Logging** (INFO/WARNING/ERROR)

Key sections:
```python
# Scraping
- scrape_internshala()
- scrape_angellist()
- scrape_linkedin_selenium()
- read_gmail_job_alerts()

# Data Management
- load_existing_internships()
- save_internships_to_excel()
- filter_new_internships()

# Enhancement
- summarize_with_gemini()

# Notifications
- send_email_notification()
```

#### requirements.txt
Dependencies:
- `requests` - HTTP requests for web scraping
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML processing
- `openpyxl` - Excel file handling
- `selenium` - Browser automation
- `google-generativeai` - Gemini API
- `imapclient` - Gmail IMAP access

#### test_setup.py (250+ lines)
Environment validation before running main.py:
- Python version check (3.8+)
- Dependency verification
- Firefox/GeckoDriver detection
- Email credential testing
- LinkedIn credential validation
- Gemini API testing
- Data directory creation

### GitHub Actions

#### .github/workflows/internship-bot.yml
Automated workflow:
- **Trigger**: Cron (4x daily) + manual
- **Runner**: ubuntu-latest
- **Steps**:
  1. Checkout code
  2. Setup Python 3.11
  3. Install Firefox + GeckoDriver
  4. Create data directory
  5. Install Python dependencies
  6. Run main.py with secrets
  7. Upload Excel artifact
  8. Upload logs artifact

### Configuration & Control

#### .gitignore
Prevents accidental commits:
- `.env` files
- Python cache (`__pycache__/`)
- Virtual environments
- Log files
- Excel output files
- IDE settings (.vscode/, .idea/)

### Documentation

#### README.md (500+ lines)
Complete user guide:
- Features overview
- Setup instructions (local & GitHub)
- Project structure
- Configuration guide
- Troubleshooting
- Security practices
- Tips and customization

#### QUICKSTART.md (100+ lines)
5-minute setup:
- Credential preparation (5 min)
- Local testing (2 min)
- GitHub Actions setup (3 min)
- Expected results
- Common issues

#### CONFIGURATION.md (400+ lines)
Detailed configuration:
- Environment variables explained
- Credential setup (Gmail, LinkedIn, Gemini)
- Local development setup
- GitHub Actions setup
- Troubleshooting for each credential type
- Security best practices
- Testing instructions

#### PROJECT_SUMMARY.md (300+ lines)
Project overview:
- Architecture diagram
- Deployment steps
- Code metrics
- Performance analysis
- Production checklist
- Future enhancements

## Data Flow

```
┌──────────────────────────────────────────┐
│     GitHub Actions (4x daily)            │
│     or Manual Trigger                    │
└────────────────┬─────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────┐
│      main.py Execution                   │
│  ┌────────────────────────────────────┐  │
│  │ 1. Read search query               │  │
│  │ 2. Load existing data              │  │
│  │ 3. Scrape sources:                 │  │
│  │    ├─ Internshala (HTTP)           │  │
│  │    ├─ AngelList (HTTP)             │  │
│  │    ├─ LinkedIn (Selenium)          │  │
│  │    └─ Gmail (IMAP)                 │  │
│  │ 4. Deduplicate results             │  │
│  │ 5. Enhance with Gemini (optional)  │  │
│  │ 6. Save to Excel                   │  │
│  │ 7. Send email                      │  │
│  └────────────────────────────────────┘  │
└────────────────┬─────────────────────────┘
                 │
    ┌────────────┼────────────┬──────────┐
    ▼            ▼            ▼          ▼
┌─────────┐ ┌────────┐ ┌─────────┐ ┌───────┐
│ Excel   │ │ Email  │ │  Logs   │ │GitHub │
│ File    │ │ Alert  │ │ Storage │ │Artifact
└─────────┘ └────────┘ └─────────┘ └───────┘
```

## Workflow Execution Timeline

```
GitHub Actions Scheduler (4x daily)
        │
        ├─ 00:00 UTC (Midnight)
        ├─ 06:00 UTC (6 AM)
        ├─ 12:00 UTC (Noon)
        └─ 18:00 UTC (6 PM)

Each execution:
  ├─ Checkout code (1 min)
  ├─ Setup environment (2 min)
  ├─ Run main.py (5-10 min)
  │  ├─ Scrape websites (2 min)
  │  ├─ Login to LinkedIn (1 min)
  │  ├─ Process data (1 min)
  │  └─ Send email (1 min)
  ├─ Upload artifacts (1 min)
  └─ Complete (9-15 min total)
```

## Environment Variables Flow

```
┌─ GitHub Actions Secrets ─┐
│ EMAIL_ADDRESS            │
│ EMAIL_PASSWORD           │
│ LINKEDIN_EMAIL           │
│ LINKEDIN_PASSWORD        │
│ GEMINI_API_KEY          │
└──────────────┬───────────┘
               │
               ▼
    os.getenv() calls in main.py
               │
    ┌──────────┼──────────┬──────────┐
    ▼          ▼          ▼          ▼
  Gmail    LinkedIn   Gemini    Search Query
  Auth      Auth       API      (optional)
```

## Key Metrics

| Metric | Value |
|--------|-------|
| Total Python code | 700+ lines |
| Functions | 15+ |
| Scraping sources | 4 |
| Documentation files | 5 |
| GitHub Actions steps | 8 |
| Environment variables | 5 |
| Error handling blocks | 20+ |
| Scheduled runs per day | 4 |
| Excel columns | 6 |
| Test checks | 7 |

## Dependencies Dependency Graph

```
main.py
  ├─ requests ─────────────────────┐
  ├─ beautifulsoup4 ───────────────┼─ Web Scraping
  ├─ selenium ─────────────────────┤
  ├─ openpyxl ─────────────────────┼─ Excel
  ├─ google-generativeai ──────────┼─ AI
  └─ imapclient ───────────────────┼─ Email (IMAP)
                                   │
                            Standard Library
                            (smtplib, logging,
                             pathlib, etc.)
```

## Security Implementation

```
User Credentials
       │
       └─ GitHub Secrets
              │
              ├─ When workflow runs
              │
              └─ Passed as ENV vars to runner
                     │
                     └─ os.getenv() in main.py
                            │
                            ├─ Never logged
                            ├─ Never hardcoded
                            └─ Never committed
```

## Output Files

```
After each run:
├─ data/internships.xlsx
│  ├─ Updated with new internships
│  ├─ Formatted with colors
│  ├─ 6 columns
│  └─ No duplicates
│
├─ internship_finder.log
│  ├─ Timestamped entries
│  ├─ DEBUG/INFO/WARNING/ERROR levels
│  ├─ Execution details
│  └─ Error messages
│
└─ GitHub Actions Artifacts
   ├─ internships.xlsx (30-day retention)
   └─ internship_finder.log (7-day retention)
```

## Getting Started Path

```
1. Clone Repository
   └─ git clone <repo>

2. Read Documentation
   ├─ README.md (full overview)
   ├─ QUICKSTART.md (5-minute setup)
   └─ CONFIGURATION.md (detailed setup)

3. Local Testing
   ├─ Create virtual environment
   ├─ Install dependencies
   ├─ Set environment variables
   ├─ Run test_setup.py
   └─ Run main.py

4. GitHub Actions Deployment
   ├─ Add GitHub Secrets
   ├─ Verify workflow
   ├─ Monitor artifacts
   └─ Receive notifications

5. Maintenance
   ├─ Monitor runs
   ├─ Check Excel file
   ├─ Update selectors if needed
   └─ Refresh credentials periodically
```

---

**Total Files**: 13  
**Total Documentation**: 5 guides + inline comments  
**Production Ready**: ✅ Yes  
**Time to Deploy**: ~10 minutes
