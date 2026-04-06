# 🌐 AutoWebPwn - Scan Any Website

AutoWebPwn can scan **ANY website** you have permission to test. This guide shows how to use it for:
- Authorized penetration testing
- Security vulnerability assessments
- Web application security audits
- Bug bounty programs (with program rules)

---

## ⚠️ IMPORTANT Legal Requirements

Before scanning ANY website:

✅ **REQUIRED:**
- [ ] You have explicit written permission to test
- [ ] You own the website OR have authorization from the owner
- [ ] Testing complies with all applicable laws
- [ ] You understand responsible disclosure

❌ **PROHIBITED:**
- Unauthorized scanning of systems you don't own
- Testing without explicit permission (even if you can access it)
- Scanning systems you don't have authority to test
- Using findings for malicious purposes

---

## 🚀 Basic Usage - Any Website

### Simple Scan
```bash
# Scan any website
python main.py -u http://example.com -o report.pdf
```

### Scan with Depth Control
```bash
# Shallow scan (1 level)
python main.py -u http://example.com -d 1 -o report_shallow.pdf

# Medium scan (2 levels)
python main.py -u http://example.com -d 2 -o report_medium.pdf

# Deep scan (3+ levels)
python main.py -u http://example.com -d 3 -o report_deep.pdf
```

### Scan with Authentication
```bash
# Use cookies for authenticated testing
python main.py -u http://example.com --cookie "session=abc123; user=john" -o report.pdf

# Use with multiple cookies
python main.py -u http://example.com --cookie "auth=token; role=admin" -o report_authenticated.pdf
```

### Scan Through Proxy
```bash
# Test through HTTP proxy (for monitoring with Burp Suite)
python main.py -u http://example.com --proxy "http://127.0.0.1:8080" -o report_proxied.pdf

# Test through SOCKS5 proxy
python main.py -u http://example.com --proxy "socks5://127.0.0.1:9050" -o report_socks.pdf
```

### Specific Module Testing
```bash
# Test only authentication bypass
python main.py -u http://example.com -m auth -o report_auth.pdf

# Test only file inclusion
python main.py -u http://example.com -m lfi -o report_lfi.pdf

# Test multiple modules
python main.py -u http://example.com -m auth,lfi -o report_modules.pdf
```

---

## 🎯 Real-World Scenarios

### Scenario 1: Corporate Web Application Audit
```bash
# Authorized audit of internal company web app
python main.py \
  -u http://internal-app.company.com \
  -d 2 \
  --cookie "session=internal_token; department=security" \
  -o corporate_audit_report.pdf
```

### Scenario 2: Bug Bounty Program
```bash
# Test target from HackerOne/Bugcrowd (with program authorization)
python main.py \
  -u http://target-program.bugbounty.com \
  -d 2 \
  --evasion \
  -o bug_bounty_findings.pdf
```

### Scenario 3: Client Security Assessment
```bash
# External penetration testing engagement
python main.py \
  -u http://client-website.com \
  -d 3 \
  --proxy "http://127.0.0.1:8080" \
  -o client_assessment.pdf
```

### Scenario 4: Development Environment Testing
```bash
# Test staging/dev environment before production
python main.py \
  -u http://staging.example.com \
  -d 2 \
  --cookie "environment=staging" \
  -o staging_security_report.pdf
```

### Scenario 5: API Security Testing
```bash
# Test REST API endpoints
python main.py \
  -u http://api.example.com/v1 \
  -d 2 \
  -o api_security_report.pdf

# With authentication token
python main.py \
  -u http://api.example.com/v1 \
  --cookie "Authorization: Bearer token123" \
  -o api_authenticated_report.pdf
```

---

## 📊 Command Reference - Any Website

### Required Parameters
```bash
-u, --url URL              Target URL (REQUIRED)
                           Can be:
                           - http://example.com
                           - https://example.com
                           - http://example.com/path/to/app
                           - http://192.168.1.100
```

### Optional Parameters
```bash
-m, --modules MODULES      Modules to run (default: all)
                           Options: auth, lfi, scanner, all

-d, --depth DEPTH          Crawling depth (default: 3)
                           1 = shallow
                           2 = medium
                           3 = deep
                           4+ = very deep

-t, --threads THREADS      Number of threads (default: 5)
                           Higher = faster but noisier

-o, --output FILE          Output report filename
                           Default: report.pdf
                           Can be any .pdf file name

--proxy PROXY              Proxy server
                           http://127.0.0.1:8080
                           socks5://127.0.0.1:9050

--cookie COOKIE            Authentication cookies
                           "session=abc; user=john"
                           "auth=token123"

--evasion                  Enable evasion techniques
                           Evade detection systems

--stealth                  Enable stealth mode
                           Slower but quieter scanning
```

---

## 💡 Common Testing Examples

### Example 1: Quick Assessment
```bash
# Fast scan of public website
python main.py -u https://example.com -d 1 -o quick_assessment.pdf
```

### Example 2: Thorough Assessment
```bash
# Complete assessment with all checks
python main.py -u https://example.com -d 3 -o thorough_assessment.pdf
```

### Example 3: Authenticated Testing
```bash
# Test with user credentials
python main.py \
  -u https://example.com/admin \
  --cookie "session=authenticated_token" \
  -d 2 \
  -o authenticated_testing.pdf
```

### Example 4: Stealthy Testing
```bash
# Slow and stealthy scan
python main.py \
  -u https://example.com \
  --stealth \
  --evasion \
  -d 2 \
  -o stealth_report.pdf
```

### Example 5: Specific Endpoint
```bash
# Test specific endpoint
python main.py -u https://example.com/login -o login_security.pdf
python main.py -u https://example.com/api/users -o api_security.pdf
```

---

## 🔐 Best Practices for Any Website Testing

### 1. Get Permission FIRST
```
Before scanning:
✅ Contact website owner
✅ Get written authorization
✅ Establish testing scope
✅ Agree on testing times
```

### 2. Use Appropriate Depth
```
Shallow (d=1):   For quick checks, minimal impact
Medium (d=2):    For balanced testing
Deep (d=3):      For comprehensive assessment
Very Deep (d=4+): For thorough analysis
```

### 3. Monitor Impact
```bash
# Start with shallow scan to assess impact
python main.py -u http://target.com -d 1 -o initial_test.pdf

# Monitor server logs during scan
# If acceptable, proceed with deeper scans
```

### 4. Use Stealth When Needed
```bash
# For sensitive environments
python main.py \
  -u http://target.com \
  --stealth \
  --evasion \
  -o stealth_report.pdf
```

### 5. Respect Rate Limits
```bash
# Use single thread for rate-limited servers
python main.py -u http://target.com -t 1 -o rate_limited.pdf

# Add evasion for protected targets
python main.py -u http://target.com --evasion -o evasion_report.pdf
```

---

## 📝 Documentation and Reporting

### Report Contents
```
✅ Scan Summary
   - Target URL
   - Scan duration
   - URLs discovered
   - Vulnerabilities found

✅ Vulnerability Details
   - Type and severity
   - Location (URL/parameter)
   - Proof of concept
   - Remediation steps

✅ Technical Findings
   - Server information
   - Technology stack
   - Security headers
   - Configuration issues
```

### Organizing Reports
```bash
# Create dated reports
python main.py -u http://target.com -o report_$(date +%Y%m%d).pdf

# Create categorized reports
python main.py -u http://target.com/admin -o admin_panel_report.pdf
python main.py -u http://target.com/api -o api_report.pdf
python main.py -u http://target.com/login -o authentication_report.pdf
```

---

## 🎯 Testing Workflow

### Step 1: Reconnaissance
```bash
# Initial scan with low depth
python main.py -u http://target.com -d 1 -o step1_reconnaissance.pdf
```

### Step 2: Initial Assessment
```bash
# Standard depth scan
python main.py -u http://target.com -d 2 -o step2_initial_assessment.pdf
```

### Step 3: Deep Analysis
```bash
# Comprehensive scan
python main.py -u http://target.com -d 3 -o step3_deep_analysis.pdf
```

### Step 4: Authenticated Testing
```bash
# Test with credentials
python main.py \
  -u http://target.com \
  --cookie "auth=session_token" \
  -o step4_authenticated_testing.pdf
```

### Step 5: API Testing
```bash
# Test API endpoints
python main.py -u http://target.com/api -d 2 -o step5_api_testing.pdf
```

---

## ⚠️ Troubleshooting Network Issues

### Connection Timeout
```bash
# Site is slow or blocking
# Try with longer timeout
python main.py -u http://target.com -d 1 -o report.pdf
```

### Rate Limiting / Blocking
```bash
# Use stealth mode
python main.py \
  -u http://target.com \
  --stealth \
  -t 1 \
  -o report.pdf
```

### Authentication Issues
```bash
# Get correct cookie format first
# 1. Access site in browser
# 2. Open Developer Tools (F12)
# 3. Go to Application > Cookies
# 4. Copy cookie values
# 5. Pass to AutoWebPwn

python main.py \
  -u http://target.com \
  --cookie "correct_session_value" \
  -o report.pdf
```

### Proxy Issues
```bash
# Verify proxy is running
# Then test with proxy
python main.py \
  -u http://target.com \
  --proxy "http://127.0.0.1:8080" \
  -o report.pdf
```

---

## 📚 Integration with Other Tools

### With Burp Suite
```bash
# Capture traffic in Burp while scanning
python main.py \
  -u http://target.com \
  --proxy "http://127.0.0.1:8080" \
  -o burp_capture_report.pdf
```

### With Custom Scripts
```bash
# Extract URLs from scan report and use in other tools
# Create wrapper script to chain tools together
```

### Multiple Target Scanning
```bash
# Create scanning script for multiple targets
for site in site1.com site2.com site3.com; do
  python main.py -u "http://$site" -o "report_$site.pdf"
done
```

---

## 🔒 Security Considerations

✅ **DO:**
- Test only authorized targets
- Document all activities
- Handle findings responsibly
- Follow disclosure procedures
- Maintain testing records

❌ **DON'T:**
- Scan without authorization
- Extract or exfiltrate data
- Modify target systems
- Publicly disclose vulnerabilities
- Use for malicious purposes

---

## 📞 Support for Custom Targets

Need help scanning a specific target? Check:
1. **Target Accessibility** - Can you reach it from your location?
2. **Authentication** - Do you have valid credentials?
3. **Permissions** - Do you have written authorization?
4. **Network** - Is your proxy/firewall correctly configured?

---

## 🎓 Learning Resources

- **DVWA Guide** - Learn with intentionally vulnerable apps first
- **OWASP Top 10** - Understand common vulnerabilities
- **Web Security Academy** - Free training course
- **PortSwigger Labs** - Practice with guided exercises

---

**Remember: AutoWebPwn is designed for AUTHORIZED TESTING ONLY. Always get permission before scanning any website.**

For legal vulnerable applications, see: **LEGAL_TESTING_EXAMPLES.md**
