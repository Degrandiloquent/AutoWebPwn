# 🛡️ AutoWebPwn - Legal Vulnerable Application Testing

This guide shows exactly how to test AutoWebPwn using safe, legal, intentionally vulnerable applications.

## ✅ Important: These are LEGAL test environments designed for security learning

All applications below are intentionally vulnerable and designed specifically for:
- Security training
- Penetration testing practice
- Vulnerability assessment learning
- Educational security research

---

## 🚀 Quick Commands

Copy and paste these exact commands to test AutoWebPwn:

### 1. DVWA (Damn Vulnerable Web Application)
```bash
# Start DVWA
docker run -d -p 80:80 vulnerables/web-dvwa

# Run AutoWebPwn scan
python main.py -u http://localhost/dvwa --cookie "security=low; PHPSESSID=xxx" -o report_dvwa.pdf

# View report
# Open report_dvwa.pdf
```

### 2. WebGoat
```bash
# Start WebGoat
docker run -d -p 8080:8080 -p 9090:9090 webgoat/goatandwolf

# Run AutoWebPwn scan
python main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf

# View report
# Open report_webgoat.pdf
```

### 3. bWAPP
```bash
# Start bWAPP
docker run -d -p 80:80 raesene/bwapp

# Run AutoWebPwn scan
python main.py -u http://localhost/bWAPP -o report_bwapp.pdf

# View report
# Open report_bwapp.pdf
```

### 4. Juice Shop
```bash
# Start Juice Shop
docker run -d -p 3000:3000 bkimminich/juice-shop

# Run AutoWebPwn scan
python main.py -u http://localhost:3000 -o report_juice_shop.pdf

# View report
# Open report_juice_shop.pdf
```

---

## 🎯 One-Command Setup (Docker Compose)

Start all vulnerable applications at once:

```bash
# Start all applications
docker-compose up -d

# Access them at:
# - DVWA: http://localhost/dvwa (admin/password)
# - WebGoat: http://localhost:8080/WebGoat
# - bWAPP: http://localhost/bWAPP (bee/bug)
# - Juice Shop: http://localhost:3000

# Run all scans
python test_runner.py all

# View reports
# - report_dvwa.pdf
# - report_webgoat.pdf
# - report_bwapp.pdf
# - report_juice_shop.pdf
```

---

## 🪟 Windows Users - Easy Menu

Simply run the batch script:

```bash
test_legal_apps.bat
```

This provides an interactive menu for:
- Starting vulnerable apps
- Running scans
- Viewing reports

---

## 📊 What to Expect

### DVWA (Beginner-Friendly)
- **Vulnerabilities**: SQL Injection, XSS, CSRF, File Inclusion
- **Difficulty**: Adjustable (Low/Medium/High/Impossible)
- **Time to scan**: ~2-3 minutes
- **Expected findings**: 10-20 vulnerabilities

### WebGoat (Interactive Learning)
- **Vulnerabilities**: OWASP Top 10 covered
- **Learning**: Step-by-step instructions included
- **Time to scan**: ~5-10 minutes
- **Expected findings**: 15-25 vulnerabilities

### bWAPP (Advanced)
- **Vulnerabilities**: 100+ intentional bugs
- **Difficulty**: Very challenging
- **Time to scan**: ~10-15 minutes
- **Expected findings**: 20-40 vulnerabilities

### Juice Shop (Modern Style)
- **Vulnerabilities**: Contemporary web app issues
- **Style**: Realistic e-commerce application
- **Time to scan**: ~5-10 minutes
- **Expected findings**: 15-30 vulnerabilities

---

## 📝 Command Examples

### Test with custom depth
```bash
python main.py -u http://localhost/dvwa -d 2 -o report.pdf
```

### Test specific modules only
```bash
python main.py -u http://localhost/dvwa -m auth,lfi -o report.pdf
```

### Test with proxy
```bash
python main.py -u http://localhost/dvwa --proxy "http://127.0.0.1:8080" -o report.pdf
```

### Multiple scans
```bash
python main.py -u http://localhost/dvwa -o dvwa1.pdf
python main.py -u http://localhost:8080/WebGoat -o webgoat1.pdf
python main.py -u http://localhost:3000 -o juice1.pdf
```

---

## 🔍 Generated Reports Include

Each PDF report contains:

✅ **Scan Summary**
- Target URL
- Scan timestamp
- URLs discovered
- Total vulnerabilities found

✅ **Vulnerability Details**
- Type of vulnerability
- Location (URL, parameter)
- Severity level
- Proof of exploitation

✅ **URL Enumeration**
- Complete list of discovered URLs
- Organized by structure
- Access patterns

✅ **Recommendations**
- Remediation steps
- Security best practices
- OWASP references

---

## 🛠️ Troubleshooting

### Docker image not found
```bash
# Pull the image first
docker pull vulnerables/web-dvwa
docker pull webgoat/goatandwolf
docker pull raesene/bwapp
docker pull bkimminich/juice-shop
```

### Port already in use
```bash
# Use different port
docker run -d -p 8080:80 vulnerables/web-dvwa
python main.py -u http://localhost:8080/dvwa
```

### Connection refused
```bash
# Check if container is running
docker ps

# Wait a moment and try again (containers need time to start)
sleep 5
```

### Python venv issues
```bash
# Recreate virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🎓 Learning Progression

1. **Start with DVWA (Low)**
   - Understand basic vulnerabilities
   - Practice with simple targets

2. **Progress to WebGoat**
   - Learn OWASP Top 10 systematically
   - Follow guided exercises

3. **Challenge yourself with Juice Shop**
   - Real-world style vulnerabilities
   - Realistic application flow

4. **Master bWAPP**
   - Discover 100+ bugs
   - Complex exploitation scenarios

---

## ⚠️ Legal & Ethical Guidelines

✅ **ALWAYS:**
- Use only these legal test environments
- Test only applications you own/have permission for
- Document all findings
- Follow responsible disclosure if finding real vulnerabilities

❌ **NEVER:**
- Test external systems without permission
- Use for unauthorized access
- Disclose vulnerabilities publicly without remediation time
- Violate any laws or regulations

---

## 📚 Additional Resources

- **README.md** - Framework overview
- **TESTING_GUIDE.md** - Detailed setup instructions
- **OWASP Top 10** - Common web vulnerabilities
- **PortSwigger Web Security** - Learning materials
- **CWE Directory** - Weakness classification

---

## 🚀 Next Steps

1. **Install Docker** (if not already installed)
2. **Choose a vulnerable app** from the options above
3. **Start the application** using the docker command
4. **Run AutoWebPwn scan** with the provided command
5. **Review the PDF report** with findings
6. **Learn** from the vulnerabilities discovered

---

**Happy secure testing! Remember: with great power comes great responsibility. 🛡️**
