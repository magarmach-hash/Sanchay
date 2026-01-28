#!/usr/bin/env python3
"""
Test script to validate environment setup.
Run this before using main.py to ensure all credentials and dependencies are correct.
"""

import os
import sys
from pathlib import Path

def test_python_version():
    """Check Python version."""
    print("🔍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor} detected. Python 3.8+ required.")
        return False


def test_dependencies():
    """Check if all required packages are installed."""
    print("\n🔍 Checking dependencies...")
    required = [
        "requests",
        "bs4",
        "openpyxl",
        "selenium",
        "google.generativeai",
        "imapclient",
    ]
    
    all_ok = True
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"✗ {package} NOT installed")
            print(f"  Run: pip install -r requirements.txt")
            all_ok = False
    
    return all_ok


def test_firefox():
    """Check if Firefox and GeckoDriver are available."""
    print("\n🔍 Checking Firefox and GeckoDriver...")
    import shutil
    
    firefox = shutil.which("firefox")
    geckodriver = shutil.which("geckodriver")
    
    if firefox:
        print(f"✓ Firefox found at: {firefox}")
    else:
        print("✗ Firefox NOT found")
        print("  Ubuntu/Debian: sudo apt-get install firefox-geckodriver")
        print("  macOS: brew install firefox geckodriver")
        return False
    
    if geckodriver:
        print(f"✓ GeckoDriver found at: {geckodriver}")
    else:
        print("✗ GeckoDriver NOT found")
        print("  Ubuntu/Debian: sudo apt-get install firefox-geckodriver")
        print("  macOS: brew install geckodriver")
        return False
    
    return True


def test_email_credentials():
    """Test Gmail SMTP and IMAP credentials."""
    print("\n🔍 Testing Gmail credentials...")
    
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    
    if not email or not password:
        print("⚠ EMAIL_ADDRESS or EMAIL_PASSWORD not set")
        print("  Set with: export EMAIL_ADDRESS='...'; export EMAIL_PASSWORD='...'")
        return None  # Not a hard failure
    
    print(f"  Using email: {email}")
    
    # Test SMTP
    try:
        import smtplib
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=5) as server:
            server.login(email, password)
        print("✓ Gmail SMTP authentication successful")
        smtp_ok = True
    except smtplib.SMTPAuthenticationError:
        print("✗ Gmail SMTP authentication failed")
        print("  Ensure you're using an app password, not your main password")
        print("  Create app password: https://myaccount.google.com/apppasswords")
        smtp_ok = False
    except Exception as e:
        print(f"⚠ Could not test SMTP: {e}")
        smtp_ok = None
    
    # Test IMAP
    try:
        import imapclient
        server = imapclient.IMAPClient("imap.gmail.com", ssl=True)
        server.login(email, password)
        server.logout()
        print("✓ Gmail IMAP authentication successful")
        imap_ok = True
    except imapclient.IMAPClient.error as e:
        print(f"✗ Gmail IMAP authentication failed: {e}")
        print("  Ensure 2FA is enabled and you're using an app password")
        imap_ok = False
    except Exception as e:
        print(f"⚠ Could not test IMAP: {e}")
        imap_ok = None
    
    return smtp_ok is True and imap_ok is True


def test_linkedin_credentials():
    """Check if LinkedIn credentials are set."""
    print("\n🔍 Checking LinkedIn credentials...")
    
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("⚠ LINKEDIN_EMAIL or LINKEDIN_PASSWORD not set")
        print("  Set with: export LINKEDIN_EMAIL='...'; export LINKEDIN_PASSWORD='...'")
        return None  # Not a hard failure
    
    print(f"  Using LinkedIn email: {email}")
    print("✓ LinkedIn credentials are set")
    print("  (Full authentication test requires interactive login)")
    return True


def test_gemini_api():
    """Test Gemini API credentials."""
    print("\n🔍 Checking Gemini API...")
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("⚠ GEMINI_API_KEY not set (optional)")
        print("  The bot works without it. Set with: export GEMINI_API_KEY='...'")
        return None
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content("Test", request_options={"timeout": 10})
        if response.text:
            print("✓ Gemini API authentication successful")
            return True
    except Exception as e:
        print(f"✗ Gemini API test failed: {e}")
        print("  Verify API key: https://makersuite.google.com/app/apikey")
        return False


def test_data_directory():
    """Check if data directory can be created."""
    print("\n🔍 Checking data directory...")
    
    data_dir = Path("data")
    try:
        data_dir.mkdir(exist_ok=True)
        print(f"✓ Data directory ready at: {data_dir.absolute()}")
        return True
    except Exception as e:
        print(f"✗ Could not create data directory: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("🧪 Internship Finder - Environment Test")
    print("=" * 60)
    
    results = {
        "Python Version": test_python_version(),
        "Dependencies": test_dependencies(),
        "Firefox/GeckoDriver": test_firefox(),
        "Email Credentials": test_email_credentials(),
        "LinkedIn Credentials": test_linkedin_credentials(),
        "Gemini API": test_gemini_api(),
        "Data Directory": test_data_directory(),
    }
    
    print("\n" + "=" * 60)
    print("📊 Test Summary")
    print("=" * 60)
    
    critical_tests = {
        "Python Version": results["Python Version"],
        "Dependencies": results["Dependencies"],
        "Firefox/GeckoDriver": results["Firefox/GeckoDriver"],
        "Data Directory": results["Data Directory"],
    }
    
    email_result = results["Email Credentials"]
    linkedin_result = results["LinkedIn Credentials"]
    gemini_result = results["Gemini API"]
    
    print("\n🔴 CRITICAL:")
    for test, result in critical_tests.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {test}")
    
    print("\n🟡 OPTIONAL/CONDITIONAL:")
    if email_result is not None:
        print(f"  {'✓ PASS' if email_result else '✗ FAIL'}: Email Credentials")
    else:
        print(f"  ⚠ SKIPPED: Email Credentials")
    
    if linkedin_result is not None:
        print(f"  {'✓ PASS' if linkedin_result else '✗ FAIL'}: LinkedIn Credentials")
    else:
        print(f"  ⚠ SKIPPED: LinkedIn Credentials")
    
    if gemini_result is not None:
        print(f"  {'✓ PASS' if gemini_result else '✗ FAIL'}: Gemini API")
    else:
        print(f"  ⚠ OPTIONAL: Gemini API")
    
    # Overall result
    critical_pass = all(critical_tests.values())
    if critical_pass:
        print("\n✅ All critical tests passed!")
        if email_result is False or linkedin_result is False:
            print("⚠️  Some credentials are not working. Review the errors above.")
            return 1
        print("You can now run: python main.py")
        return 0
    else:
        print("\n❌ Some critical tests failed. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
