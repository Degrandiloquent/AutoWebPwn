#!/usr/bin/env python3
"""
AutoWebPwn - Legal Vulnerable Application Testing Quick Reference
This file shows exactly how to test AutoWebPwn against legal vulnerable apps
"""

# =============================================================================
# IMPORTANT: Before running any scans, start the vulnerable applications
# =============================================================================

import subprocess
import sys
import platform

COMMANDS = {
    'dvwa': {
        'description': 'DVWA (Damn Vulnerable Web Application) - Low Security',
        'docker_start': 'docker run -d -p 80:80 vulnerables/web-dvwa',
        'scan_command': 'python main.py -u http://localhost/dvwa --cookie "security=low; PHPSESSID=xxx" -o report_dvwa.pdf',
        'access_url': 'http://localhost/dvwa',
        'default_creds': 'admin / password'
    },
    'webgoat': {
        'description': 'WebGoat (OWASP Interactive Learning Platform)',
        'docker_start': 'docker run -d -p 8080:8080 -p 9090:9090 webgoat/goatandwolf',
        'scan_command': 'python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf',
        'access_url': 'http://localhost:8080/WebGoat',
        'default_creds': 'None (interactive learning)'
    },
    'bwapp': {
        'description': 'bWAPP (Buggy Web Application) - 100+ intentional bugs',
        'docker_start': 'docker run -d -p 80:80 raesene/bwapp',
        'scan_command': 'python main.py -u http://localhost/bWAPP -o report_bwapp.pdf',
        'access_url': 'http://localhost/bWAPP',
        'default_creds': 'bee / bug'
    },
    'juice': {
        'description': 'Juice Shop (OWASP Modern Vulnerable Application)',
        'docker_start': 'docker run -d -p 3000:3000 bkimminich/juice-shop',
        'scan_command': 'python main.py -u http://localhost:3000 -o report_juice_shop.pdf',
        'access_url': 'http://localhost:3000',
        'default_creds': 'None (intentionally vulnerable e-commerce)'
    }
}

def print_header():
    print("\n" + "="*80)
    print("  🛡️  AutoWebPwn - Legal Vulnerable Application Testing Guide")
    print("="*80)

def show_quick_start():
    print("\n📋 QUICK START - Testing Legal Vulnerable Applications\n")
    
    for app, info in COMMANDS.items():
        print(f"\n{info['description']}")
        print("-" * 80)
        print(f"1. Start the application:")
        print(f"   {info['docker_start']}")
        print(f"\n2. Access at: {info['access_url']}")
        print(f"   Credentials: {info['default_creds']}")
        print(f"\n3. Run AutoWebPwn scan:")
        print(f"   {info['scan_command']}")
        print(f"\n4. View report: report_{app.replace('juice', 'juice_shop')}.pdf")

def show_batch_testing():
    print("\n\n🚀 BATCH TESTING - Run All Scans\n")
    print("Option 1: Using test_runner.py")
    print("  python test_runner.py all")
    print("\nOption 2: Using docker-compose")
    print("  docker-compose up -d")
    print("  python test_runner.py all")

def show_commands():
    print("\n\n📝 COMMAND REFERENCE\n")
    
    print("1. DVWA (Damn Vulnerable Web Application)")
    print("   " + COMMANDS['dvwa']['scan_command'])
    
    print("\n2. WebGoat (OWASP Interactive Learning)")
    print("   " + COMMANDS['webgoat']['scan_command'])
    
    print("\n3. bWAPP (Buggy Web Application)")
    print("   " + COMMANDS['bwapp']['scan_command'])
    
    print("\n4. Juice Shop (OWASP Modern Vulnerable App)")
    print("   " + COMMANDS['juice']['scan_command'])

def main():
    print_header()
    show_quick_start()
    show_batch_testing()
    show_commands()
    
    print("\n\n" + "="*80)
    print("📚 For detailed information, see:")
    print("   - README.md - Framework overview")
    print("   - TESTING_GUIDE.md - Detailed setup instructions")
    print("   - docker-compose.yml - One-command setup for all apps")
    print("="*80 + "\n")

if __name__ == '__main__':
    main()
