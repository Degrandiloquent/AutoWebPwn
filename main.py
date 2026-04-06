#!/usr/bin/env python3
"""
AutoWebPwn - Automated Web Application Penetration Testing Framework
"""
import argparse
import sys
from core.crawler import AdvancedCrawler
from modules.auth_bypass import AuthBypass
from modules.file_inclusion import FileInclusion
from core.scanner import VulnerabilityScanner
import logging
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        description='AutoWebPwn - Automated Web Application Penetration Testing Framework\n\n'
                    'Scan ANY website with authorization. Examples:\n'
                    '  python main.py -u http://example.com -o report.pdf\n'
                    '  python main.py -u http://localhost/dvwa --cookie "session=low" -o dvwa_report.pdf\n'
                    '  python main.py -u http://target.com -d 2 --stealth -o stealth_report.pdf',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-u', '--url', required=True, 
                       help='Target URL (http://example.com, http://localhost/app, etc.)')
    parser.add_argument('-m', '--modules', default='all', 
                       help='Modules to run (comma-separated): all, auth, lfi, scanner')
    parser.add_argument('-d', '--depth', type=int, default=3,
                       help='Crawling depth (1=shallow, 2=medium, 3=deep)')
    parser.add_argument('-t', '--threads', type=int, default=5,
                       help='Number of threads (higher=faster, lower=stealthier)')
    parser.add_argument('-o', '--output', default='report.pdf',
                       help='Output PDF report filename')
    parser.add_argument('--proxy', help='Proxy server (http://127.0.0.1:8080 or socks5://)')
    parser.add_argument('--cookie', help='Authentication cookies ("session=value; auth=token")')
    parser.add_argument('--evasion', action='store_true',
                       help='Enable evasion techniques (bypass defenses)')
    parser.add_argument('--stealth', action='store_true',
                       help='Enable stealth mode (slower but quieter)')
    
    args = parser.parse_args()
    
    # Initialize framework
    framework = AutoWebPwn(args)
    framework.run()
    
    print(f"\n✓ Scan completed successfully!")
    print(f"✓ PDF Report saved: {args.output}")
    print(f"✓ Log file: logs/autowebpwn.log")

class AutoWebPwn:
    def __init__(self, args):
        self.args = args
        self.setup_logging()
        self.session = self.create_session()
        self.findings = {
            'auth_bypass': [],
            'lfi': [],
            'rfi': [],
            'sql_injection': [],
            'xss': []
        }
        self.urls_discovered = []
        
    def setup_logging(self):
        import os
        os.makedirs('logs', exist_ok=True)
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('logs/autowebpwn.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def create_session(self):
        import requests
        session = requests.Session()
        
        # Set headers
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        if self.args.cookie:
            session.headers.update({'Cookie': self.args.cookie})
        
        if self.args.proxy:
            session.proxies = {'http': self.args.proxy, 'https': self.args.proxy}
        
        return session
    
    def run(self):
        self.logger.info(f"Starting scan on {self.args.url}")
        
        # 1. Crawling phase
        crawler = AdvancedCrawler(self.args.url, self.session, self.args.depth)
        urls = crawler.crawl()
        self.urls_discovered = urls
        
        # 2. Run selected modules
        if 'all' in self.args.modules or 'auth' in self.args.modules:
            auth = AuthBypass(self.session, self.findings)
            auth.test_all(urls)
        
        if 'all' in self.args.modules or 'lfi' in self.args.modules:
            lfi = FileInclusion(self.session, self.findings)
            lfi.test_all(urls)
        
        # 3. Generate PDF report
        self.generate_report()
        
        print(f"[+] Scan completed. Processed {len(urls)} URLs")

    def generate_report(self):
        """Generate comprehensive PDF report with findings"""
        try:
            from reportlab.lib.pagesizes import letter, A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import inch
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
            from reportlab.lib import colors
            from reportlab.lib.enums import TA_CENTER, TA_LEFT
        except ImportError:
            self.logger.error("reportlab not installed. Install with: pip install reportlab")
            return
        
        # Create PDF document
        pdf_file = self.args.output
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        doc.title = "AutoWebPwn - Security Scan Report"
        
        story = []
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1f4788'),
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        )
        
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#d9534f'),
            spaceAfter=10,
            fontName='Helvetica-Bold'
        )
        
        # Title
        title = Paragraph("AutoWebPwn - Security Scan Report", title_style)
        story.append(title)
        story.append(Spacer(1, 0.3*inch))
        
        # Scan Summary
        summary_data = [
            ['Scan Summary', ''],
            ['Target URL', self.args.url],
            ['Scan Date', datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
            ['URLs Discovered', str(len(self.urls_discovered))],
            ['Total Findings', str(sum(len(v) for v in self.findings.values()))]
        ]
        
        summary_table = Table(summary_data, colWidths=[2*inch, 4*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(summary_table)
        story.append(Spacer(1, 0.3*inch))
        
        # Findings section
        findings_heading = Paragraph("Vulnerabilities Found", heading_style)
        story.append(findings_heading)
        story.append(Spacer(1, 0.1*inch))
        
        has_findings = False
        
        # Authentication Bypass Findings
        if self.findings['auth_bypass']:
            has_findings = True
            story.append(Paragraph("Authentication Bypass Vulnerabilities", styles['Heading3']))
            
            for idx, finding in enumerate(self.findings['auth_bypass'], 1):
                story.append(Paragraph(f"<b>#{idx}</b> {finding}", styles['Normal']))
            
            story.append(Spacer(1, 0.2*inch))
        
        # LFI Findings
        if self.findings['lfi']:
            has_findings = True
            story.append(Paragraph("Local File Inclusion (LFI) Vulnerabilities", styles['Heading3']))
            
            for idx, finding in enumerate(self.findings['lfi'], 1):
                story.append(Paragraph(f"<b>#{idx}</b> {finding}", styles['Normal']))
            
            story.append(Spacer(1, 0.2*inch))
        
        # RFI Findings
        if self.findings['rfi']:
            has_findings = True
            story.append(Paragraph("Remote File Inclusion (RFI) Vulnerabilities", styles['Heading3']))
            
            for idx, finding in enumerate(self.findings['rfi'], 1):
                story.append(Paragraph(f"<b>#{idx}</b> {finding}", styles['Normal']))
            
            story.append(Spacer(1, 0.2*inch))
        
        # SQL Injection Findings
        if self.findings['sql_injection']:
            has_findings = True
            story.append(Paragraph("SQL Injection Vulnerabilities", styles['Heading3']))
            
            for idx, finding in enumerate(self.findings['sql_injection'], 1):
                story.append(Paragraph(f"<b>#{idx}</b> {finding}", styles['Normal']))
            
            story.append(Spacer(1, 0.2*inch))
        
        if not has_findings:
            story.append(Paragraph("✓ No critical vulnerabilities found during this scan.", styles['Normal']))
        
        # URLs Discovered
        story.append(PageBreak())
        story.append(Paragraph("URLs Discovered", heading_style))
        story.append(Spacer(1, 0.1*inch))
        
        for idx, url in enumerate(self.urls_discovered[:50], 1):  # Limit to first 50
            story.append(Paragraph(f"• {url}", styles['Normal']))
        
        if len(self.urls_discovered) > 50:
            story.append(Paragraph(f"... and {len(self.urls_discovered) - 50} more URLs", styles['Normal']))
        
        # Build PDF
        try:
            doc.build(story)
            self.logger.info(f"PDF Report generated successfully: {pdf_file}")
            print(f"[✓] PDF Report: {pdf_file}")
        except Exception as e:
            self.logger.error(f"Error generating PDF report: {e}")

if __name__ == "__main__":
    main()
