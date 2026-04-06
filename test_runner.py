#!/usr/bin/env python3
"""
AutoWebPwn - Quick Testing Script for Legal Vulnerable Applications
This script helps rapidly test AutoWebPwn against local vulnerable applications.
"""

import subprocess
import sys
import os

# Define legal vulnerable applications for testing
TEST_TARGETS = {
    'dvwa': {
        'url': 'http://localhost/dvwa',
        'args': ['--cookie', 'security=low; PHPSESSID=xxx'],
        'output': 'report_dvwa.pdf',
        'description': 'DVWA (Low Security)'
    },
    'webgoat': {
        'url': 'http://localhost:8080/WebGoat',
        'args': [],
        'output': 'report_webgoat.pdf',
        'description': 'OWASP WebGoat'
    },
    'bwapp': {
        'url': 'http://localhost/bWAPP',
        'args': [],
        'output': 'report_bwapp.pdf',
        'description': 'bWAPP'
    },
    'juice': {
        'url': 'http://localhost:3000',
        'args': [],
        'output': 'report_juice_shop.pdf',
        'description': 'OWASP Juice Shop'
    }
}

def print_header():
    print("\n" + "="*60)
    print("  AutoWebPwn - Legal Vulnerable App Testing")
    print("="*60)
    print("\nAvailable targets:\n")
    
    for idx, (key, target) in enumerate(TEST_TARGETS.items(), 1):
        print(f"  {idx}. {target['description']}")
        print(f"     URL: {target['url']}")
        print(f"     Report: {target['output']}\n")

def print_usage():
    print("\nUsage:")
    print("  python test_runner.py [target_name] [scan_depth]")
    print("\nExamples:")
    print("  python test_runner.py dvwa")
    print("  python test_runner.py webgoat 2")
    print("  python test_runner.py all")
    print("  python test_runner.py juice 1")

def run_scan(target_key, depth=3):
    """Run AutoWebPwn scan against a target"""
    if target_key not in TEST_TARGETS:
        print(f"\n❌ Unknown target: {target_key}")
        return False
    
    target = TEST_TARGETS[target_key]
    
    print(f"\n{'='*60}")
    print(f"🔍 Scanning: {target['description']}")
    print(f"{'='*60}")
    print(f"Target URL: {target['url']}")
    print(f"Scan Depth: {depth}")
    print(f"Output: {target['output']}")
    print(f"{'='*60}\n")
    
    # Build command
    cmd = [
        sys.executable,
        'main.py',
        '-u', target['url'],
        '-d', str(depth),
        '-o', target['output']
    ]
    
    # Add additional arguments (like cookies)
    cmd.extend(target['args'])
    
    print(f"Running: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(cmd, check=True)
        print(f"\n✅ Scan completed successfully!")
        print(f"📄 Report saved: {target['output']}\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Scan failed with error code: {e.returncode}\n")
        return False
    except FileNotFoundError:
        print(f"\n❌ main.py not found. Make sure you're in the AutoWebPwn directory.\n")
        return False

def main():
    if len(sys.argv) < 2:
        print_header()
        print_usage()
        sys.exit(1)
    
    target = sys.argv[1].lower()
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    print_header()
    
    # Validate depth
    if depth < 1 or depth > 5:
        print("\n⚠️  Scan depth should be between 1 and 5")
        depth = 3
    
    if target == 'all':
        print("\n🚀 Running scans on ALL targets...\n")
        results = {}
        for key in TEST_TARGETS.keys():
            results[key] = run_scan(key, depth)
        
        print("\n" + "="*60)
        print("📊 SCAN SUMMARY")
        print("="*60)
        for key, success in results.items():
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} - {TEST_TARGETS[key]['description']}")
        print("="*60 + "\n")
    else:
        success = run_scan(target, depth)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
