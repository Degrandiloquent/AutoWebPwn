# 🚀 Deploy AutoWebPwn to Vercel

This guide shows how to deploy AutoWebPwn as a web service on Vercel for easy access.

## ✨ Features

- 🌐 Web interface for scanning
- 📊 Real-time progress tracking
- 📥 PDF report generation and download
- 🔐 Authorization confirmation
- ⚡ Serverless deployment
- 📱 Mobile-friendly interface

## 📋 Prerequisites

- GitHub account with AutoWebPwn repository
- Vercel account (free tier available)
- Vercel CLI (optional, Vercel dashboard works too)

## 🔧 Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Easiest)

1. **Go to Vercel**
   - Visit https://vercel.com
   - Click "Sign Up" or login with GitHub
   - Authorize Vercel to access your GitHub

2. **Import Project**
   - Click "New Project"
   - Select your `AutoWebPwn` repository
   - Vercel auto-detects it's a Python project
   - Click "Deploy"

3. **Wait for Deployment**
   - Takes 2-3 minutes
   - Vercel builds and deploys automatically
   - You'll get a live URL (e.g., `https://autowebpwn-xxx.vercel.app`)

### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from project directory
cd c:\Users\xihlu\OneDrive\Documents\AutoWebPwn
vercel

# Follow prompts and deploy
```

## 🌐 Using the Deployed Tool

Once deployed, visit your Vercel URL and:

1. **Enter Target URL**
   - Example: `http://localhost/dvwa` (for local testing)
   - Or any authorized target

2. **Configure Options**
   - **Depth**: 1 (shallow), 2 (medium), 3 (deep)
   - **Threads**: 1 (stealthy), 3 (balanced), 5 (fast)
   - **Modules**: All or specific vulnerability tests
   - **Authentication**: Provide cookies if needed
   - **Stealth Mode**: Enabled by default (slower but quieter)

3. **Confirm Authorization**
   - Check the authorization checkbox
   - You confirm you have explicit permission to test

4. **Start Scan**
   - Click the scan button
   - Watch real-time progress
   - Get results with vulnerability count

5. **Download Report**
   - When complete, download PDF report
   - Contains all findings and details

## 📊 API Endpoints

The deployed service provides REST APIs:

### Start Scan
```bash
curl -X POST https://your-vercel-url/api/scan \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://target.com",
    "depth": 2,
    "authorized": true
  }'

# Response:
{
  "job_id": "abc123",
  "status": "started"
}
```

### Check Status
```bash
curl https://your-vercel-url/api/scan/abc123

# Response:
{
  "job_id": "abc123",
  "status": "running",
  "progress": 45,
  "url": "http://target.com"
}
```

### Get Report
```bash
curl https://your-vercel-url/api/scan/abc123/report > report.pdf
```

## ⚙️ Environment Variables

Optional: Add to Vercel dashboard for customization:

```
MAX_SCAN_DEPTH=3          # Maximum depth allowed
MAX_THREADS=5             # Maximum threads allowed
SCAN_TIMEOUT=1800         # Timeout in seconds (30 mins)
```

## 📝 Important Notes

⚠️ **Legal & Ethics:**
- Only scan targets you own or have written authorization for
- The tool requires explicit confirmation of authorization
- Unauthorized scanning is illegal and unethical
- Use responsibly for security testing only

## 🧪 Testing Before Deployment

Test locally first:

```bash
# Install dependencies
pip install -r requirements.txt
pip install flask

# Run API locally
python api.py

# Visit http://localhost:5000
```

## 🐛 Troubleshooting

### Deployment fails
- Check Python version requirements
- Verify `requirements.txt` has all dependencies
- Review Vercel build logs

### Scans timeout
- Reduce depth setting
- Use stealth mode (adds time but reduces detection)
- Split into smaller targeted scans

### PDF not generating
- Verify reportlab is in requirements.txt
- Check scan actually found something
- Review server logs

## 📈 Performance Considerations

**Vercel Serverless:**
- Free tier: Cold starts may take 10-30 seconds first run
- Scans run sequentially (not parallel across instances)
- Deep scans may timeout (>30 seconds)
- Recommended: Use depth=1 or 2 for web deployment

**Improvements:**
- Use background jobs service (AWS SQS, etc.)
- Implement result caching
- Add scan queuing system
- Use dedicated server for complex scans

## 🔄 Continuous Deployment

Every time you push to GitHub main branch:
- Vercel auto-rebuilds
- Tests your changes
- Deploys if successful
- Live immediately

## 🎯 Next Steps

1. ✅ Deploy to Vercel
2. 🧪 Test with a legal app (DVWA, WebGoat, etc.)
3. 📤 Share URL with authorized testers
4. 📊 Monitor usage and results
5. 🔧 Customize as needed

## 📞 Support

- **Vercel Docs**: https://vercel.com/docs
- **GitHub Issues**: Post to AutoWebPwn repository
- **Community**: Check discussions/forums

---

**Your Live URL Format:** `https://autowebpwn-[username].vercel.app`

Start scanning: Visit your deployed URL and begin testing!
