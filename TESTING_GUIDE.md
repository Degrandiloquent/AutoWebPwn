# AutoWebPwn Testing Guide

This guide provides instructions for testing AutoWebPwn with legal, intentionally vulnerable web applications.

## ✅ Legal Vulnerable Applications for Testing

These applications are designed specifically for security training and testing:

### 1. DVWA (Damn Vulnerable Web Application)
**Purpose:** Learning web application security vulnerabilities
**Security Levels:** Low, Medium, High, Impossible

**Setup:**
```bash
# Docker installation (recommended)
docker pull vulnerables/web-dvwa
docker run -d -p 80:80 vulnerables/web-dvwa

# Access: http://localhost/dvwa
# Default credentials: admin / password
```

**Test with AutoWebPwn:**
```bash
python main.py -u http://localhost/dvwa --cookie "security=low; PHPSESSID=xxx" -o report_dvwa.pdf
```

---

### 2. WebGoat
**Purpose:** OWASP's interactive learning platform for web security
**Features:** Guided lessons on OWASP Top 10

**Setup:**
```bash
# Docker installation
docker pull webgoat/goatandwolf
docker run -d -p 8080:8080 -p 9090:9090 webgoat/goatandwolf

# Access: http://localhost:8080/WebGoat
```

**Test with AutoWebPwn:**
```bash
python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf
```

---

### 3. bWAPP (buggy Web Application)
**Purpose:** Practice discovering and exploiting web vulnerabilities
**Vulnerabilities:** 100+ intentional bugs

**Setup:**
```bash
# Docker installation
docker pull raesene/bwapp
docker run -d -p 80:80 raesene/bwapp

# Access: http://localhost/bwapp
# Default credentials: bee / bug
```

**Test with AutoWebPwn:**
```bash
python main.py -u http://localhost/bWAPP -o report_bwapp.pdf
```

---

### 4. OWASP Juice Shop
**Purpose:** Safe environment to practice exploiting modern web vulnerabilities
**Technology:** Node.js / Angular-based boutique application

**Setup:**
```bash
# Docker installation (recommended)
docker pull bkimminich/juice-shop
docker run -d -p 3000:3000 bkimminich/juice-shop

# Access: http://localhost:3000
```

**Test with AutoWebPwn:**
```bash
python main.py -u http://localhost:3000 -o report_juice_shop.pdf
```

---

## 🚀 Quick Start Testing

### Option 1: Using Docker Compose
Create a `docker-compose.yml`:
```yaml
version: '3'
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "80:80"
  
  webgoat:
    image: webgoat/goatandwolf
    ports:
      - "8080:8080"
      - "9090:9090"
  
  juice-shop:
    image: bkimminich/juice-shop
    ports:
      - "3000:3000"
```

Run all services:
```bash
docker-compose up -d
```

### Option 2: Run Individual Scans
```bash
# Test DVWA
python main.py -u http://localhost/dvwa --cookie "security=low" -o report_dvwa.pdf

# Test WebGoat
python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf

# Test Juice Shop
python main.py -u http://localhost:3000 -o report_juice_shop.pdf
```

---

## 📊 Expected Findings

### Typical vulnerabilities AutoWebPwn should detect:

**On DVWA (Low Security):**
- SQL Injection (via form fields)
- Brute Force (login attempts)
- CSRF vulnerabilities
- File Inclusion vulnerabilities

**On Juice Shop:**
- Path Traversal
- Insecure Direct Object References (IDOR)
- Broken Authentication
- XSS vulnerabilities

**On WebGoat:**
- SQL Injection
- XSS
- Broken Authentication

---

## 🔍 Analyzing Reports

After each scan completes, review the generated PDF report:
- **report_dvwa.pdf** - DVWA findings
- **report_webgoat.pdf** - WebGoat findings
- **report_bwapp.pdf** - bWAPP findings
- **report_juice_shop.pdf** - Juice Shop findings

Each report includes:
- Scan summary and timestamp
- Discovered URLs
- Identified vulnerabilities
- Vulnerability severity and details

---

## ⚠️ Important Notes

1. **Only Use Locally:** Only test against applications running on localhost
2. **Legal Compliance:** Always ensure you have permission before testing any web application
3. **Educational Purpose:** These applications should only be used for learning
4. **Isolation:** Keep vulnerable applications isolated from production systems

---

## 🎓 Security Learning Resources

- **OWASP Top 10:** Common web application vulnerabilities
- **CWE (Common Weakness Enumeration):** Standardized weakness descriptions
- **CVSS Scoring:** Vulnerability severity rating system
- **Penetration Testing Ethics:** Responsible disclosure practices

---

## ✋ Responsible Disclosure

If you find real vulnerabilities:
1. Do NOT publicly disclose the vulnerability
2. Contact the organization's security team directly
3. Allow time for remediation before public disclosure
4. Follow responsible disclosure guidelines

---

**Happy Secure Testing! 🛡️**
