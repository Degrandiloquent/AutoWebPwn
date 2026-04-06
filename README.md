# 🛡️ AutoWebPwn - Automated Web Application Penetration Testing Framework

**Note:** This framework is designed for **legal, authorized security testing only**. Always obtain explicit permission before testing any web application.

## ⚠️ Legal & Ethical Disclaimer

```
AutoWebPwn is an educational and authorized penetration testing tool.
Unauthorized access to computer systems is illegal. 
Only use this framework to test applications you own or have explicit 
written permission to test.
```

---

## 📋 Overview

AutoWebPwn is an automated framework for discovering and testing common web application vulnerabilities. It combines web crawling, vulnerability scanning, and reporting capabilities into a single integrated tool.

### Key Features
- 🕷️ **Intelligent Web Crawling** - Recursively discovers URLs with domain restrictions
- 🔍 **Vulnerability Detection** - Tests for SQL injection, authentication bypass, file inclusion
- 📊 **PDF Report Generation** - Professional vulnerability reports with findings
- 🎯 **Modular Design** - Easy to extend with custom testing modules
- 🕐 **Stealth Testing** - Random delays and evasion techniques built-in
- 📁 **Comprehensive Logging** - Detailed logs for forensic analysis

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or download the project
cd AutoWebPwn

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Scan ANY Website (With Authorization)

AutoWebPwn can scan **any website you have permission to test**:

```bash
# Scan any website (you must have authorization!)
python main.py -u http://example.com -o report.pdf

# With custom options
python main.py -u http://example.com -d 2 --cookie "session=token" -o report.pdf

# With authentication and stealth
python main.py \
  -u http://target.example.com \
  --cookie "auth=value" \
  --stealth \
  -o comprehensive_report.pdf
```

**⚠️ IMPORTANT:** You must have explicit written permission to scan any target.

See **SCAN_ANY_WEBSITE.md** for comprehensive guidance on scanning any website including:
- Real-world testing scenarios
- Authentication handling
- Proxy configuration
- Rate limiting
- Best practices

### 3. Using Legal Test Applications

The **recommended** approach is to test against legal, intentionally vulnerable applications:

```bash
# Start all test applications (requires Docker)
docker-compose up -d

# Run scans against safe test targets
python main.py -u http://localhost/dvwa -o report_dvwa.pdf
python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf
python main.py -u http://localhost:3000 -o report_juice_shop.pdf
```

### 4. Using the Test Runner

```bash
# Test all vulnerable applications
python test_runner.py all

# Test a specific application
python test_runner.py dvwa 2
python test_runner.py juice 3

# Options:
# - dvwa: DVWA (Damn Vulnerable Web Application)
# - webgoat: OWASP WebGoat
# - bwapp: bWAPP
# - juice: OWASP Juice Shop
```

---

## 📚 Supported Legal Test Targets

### DVWA (Damn Vulnerable Web Application)
- **Purpose:** Learning web vulnerabilities with adjustable difficulty
- **Setup:** `docker run -d -p 80:80 vulnerables/web-dvwa`
- **Command:** `python main.py -u http://localhost/dvwa -o report_dvwa.pdf`

### WebGoat (OWASP)
- **Purpose:** Interactive web security training
- **Setup:** `docker run -d -p 8080:8080 webgoat/goatandwolf`
- **Command:** `python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf`

### bWAPP
- **Purpose:** Practice discovering 100+ intentional bugs
- **Setup:** `docker run -d -p 81:80 raesene/bwapp`
- **Command:** `python main.py -u http://localhost/bWAPP -o report_bwapp.pdf`

### Juice Shop (OWASP)
- **Purpose:** Modern vulnerable web application
- **Setup:** `docker run -d -p 3000:3000 bkimminich/juice-shop`
- **Command:** `python main.py -u http://localhost:3000 -o report_juice_shop.pdf`

---

## 🎯 Command Line Usage

```bash
python main.py [options]

Options:
  -u, --url URL              Target URL (required)
  -m, --modules MODULES      Modules to run: all, auth, lfi (default: all)
  -d, --depth DEPTH          Crawling depth (default: 3)
  -t, --threads THREADS      Number of threads (default: 5)
  -o, --output FILE          Output report filename (default: report.pdf)
  --proxy PROXY              HTTP/HTTPS proxy server
  --cookie COOKIE            Authentication cookies
  --evasion                  Enable evasion techniques
  --stealth                  Enable stealth mode

Examples:
  # Basic scan
  python main.py -u http://localhost/dvwa -o report.pdf
  
  # Scan with authentication
  python main.py -u http://localhost/dvwa --cookie "security=low" -o report.pdf
  
  # Scan with custom depth
  python main.py -u http://localhost:3000 -d 2 -o report.pdf
  
  # Scan specific modules only
  python main.py -u http://localhost/bWAPP -m auth,lfi -o report.pdf
```

---

## 📊 Generated Reports

AutoWebPwn generates comprehensive PDF reports containing:

```
├── Scan Summary
│   ├── Target URL
│   ├── Scan Date/Time
│   ├── URLs Discovered
│   └── Total Findings
├── Vulnerability Findings
│   ├── Authentication Bypass Issues
│   ├── Local File Inclusion (LFI)
│   ├── Remote File Inclusion (RFI)
│   └── SQL Injection Vulnerabilities
└── URL Enumeration
    └── Complete list of discovered URLs
```

---

## 🔐 Security Best Practices

1. **Always Get Permission**
   - Written authorization required before testing
   - Save all agreements for legal protection

2. **Use Legal Test Environments**
   - DVWA, WebGoat, bWAPP, Juice Shop
   - Never test production systems without approval

3. **Responsible Disclosure**
   - If finding real vulnerabilities, contact vendor privately
   - Allow time for remediation before disclosure
   - Never publicly disclose until patched

4. **Maintain Anonymity**
   - Use appropriate proxy/VPN if needed
   - Avoid personal identification
   - Follow all applicable laws

5. **Document Everything**
   - Keep detailed test logs
   - Document all findings
   - Maintain chain of custody

---

## 📁 Project Structure

```
AutoWebPwn/
├── main.py                 # Entry point and framework orchestrator
├── core/
│   ├── crawler.py         # Web crawling engine
│   └── scanner.py         # Vulnerability scanning
├── modules/
│   ├── auth_bypass.py     # Authentication testing
│   └── file_inclusion.py  # LFI/RFI testing
├── config/
│   └── config.yaml        # Framework configuration
├── logs/
│   └── autowebpwn.log    # Detailed scan logs
├── docker-compose.yml     # Quick setup for test apps
├── test_runner.py         # Batch testing script
├── TESTING_GUIDE.md       # Detailed testing documentation
└── requirements.txt       # Python dependencies
```

---

## 🔧 Configuration

Edit `config/config.yaml` to customize:
- Scan depth and threading
- Payload selection and intensity
- Evasion and stealth techniques
- Proxy and authentication settings
- Custom headers

---

## 📦 Dependencies

- **requests** - HTTP library
- **beautifulsoup4** - HTML parsing
- **reportlab** - PDF generation
- **PyJWT** - JWT token handling
- **selenium** - JavaScript rendering
- **pyyaml** - Configuration management

---

## 🐛 Troubleshooting

### Connection Timeouts
```bash
# Increase timeout in scan parameters
python main.py -u http://target -d 1 -o report.pdf
```

### Docker Issues
```bash
# Check if containers are running
docker ps

# View container logs
docker logs autowebpwn-dvwa

# Restart services
docker-compose restart
```

### Permission Errors
```bash
# Ensure proper file permissions
chmod +x main.py test_runner.py
```

---

## 🎓 Learning Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE (Common Weakness Enumeration)](https://cwe.mitre.org/)
- [Web Application Security](https://portswigger.net/web-security)
- [Penetration Testing Framework](https://www.pentest-standard.org/)

---

## 📝 License & Terms

This tool is provided for educational and authorized testing purposes only.
Users are responsible for compliance with all applicable laws and regulations.

---

## ✅ Responsible Use Checklist

- [ ] I have read and understand the legal disclaimer
- [ ] I have written authorization to test the target
- [ ] I will only test on legal, designated vulnerable applications
- [ ] I understand password security and won't use this tool illegally
- [ ] I will maintain detailed documentation of my testing
- [ ] I will follow responsible disclosure practices
- [ ] I understand the legal consequences of unauthorized access

---

## 🤝 Contributing

To contribute improvements to AutoWebPwn:
1. Ensure all tests pass
2. Follow Python best practices
3. Document your changes
4. Submit with clear description

---

## 📧 Support

For issues, questions, or suggestions:
- Review the TESTING_GUIDE.md
- Check the logs/ directory for detailed error messages
- Ensure all dependencies are properly installed

---

**Remember:** With great power comes great responsibility. Use this tool ethically and legally. 🛡️
# AutoWebPwn
