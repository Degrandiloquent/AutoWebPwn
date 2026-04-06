import re
import time
import random
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import logging

class AdvancedCrawler:
    def __init__(self, base_url, session, max_depth=3, web_mode=False):
        self.base_url = base_url
        self.session = session
        self.max_depth = max_depth
        self.visited = set()
        self.urls = []
        self.logger = logging.getLogger(__name__)
        self.web_mode = web_mode  # Fast mode for web deployment
        self.url_limit = 10 if web_mode else 100  # Limit URLs for web
        
    def crawl(self):
        self._crawl_recursive(self.base_url, 0)
        # Limit URLs for web mode to ensure quick scans
        if self.web_mode:
            self.urls = self.urls[:self.url_limit]
        return self.urls
    
    def _crawl_recursive(self, url, depth):
        # Stop if we have enough URLs in web mode
        if self.web_mode and len(self.urls) >= self.url_limit:
            return
            
        if depth > self.max_depth or url in self.visited:
            return
        
        self.visited.add(url)
        self.logger.info(f"Crawling: {url}")
        
        try:
            # Shorter delay for web mode, longer for stealth
            if self.web_mode:
                time.sleep(random.uniform(0.05, 0.2))  # Fast for web
            else:
                time.sleep(random.uniform(0.5, 2.0))   # Stealth for local
            
            # Shorter timeout for web deployment (3s instead of 10s)
            timeout = 3 if self.web_mode else 10
            response = self.session.get(url, timeout=timeout)
            
            if response.status_code == 200:
                self.urls.append(url)
                
                # Extract links
                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)
                
                for link in links:
                    href = link['href']
                    full_url = urljoin(url, href)
                    
                    # Only follow links from same domain
                    if self._is_same_domain(full_url):
                        self._crawl_recursive(full_url, depth + 1)
                
                # Extract forms
                forms = soup.find_all('form')
                for form in forms:
                    form_url = urljoin(url, form.get('action', url))
                    self.urls.append(form_url)
                    
        except Exception as e:
            self.logger.error(f"Error crawling {url}: {e}")
    
    def _is_same_domain(self, url):
        base_domain = urlparse(self.base_url).netloc
        url_domain = urlparse(url).netloc
        return base_domain == url_domain or url_domain.endswith(base_domain)
    
    def extract_js_endpoints(self, html_content):
        """Extract endpoints from JavaScript files"""
        endpoints = []
        
        # Look for API endpoints in JS
        patterns = [
            r'["\'](/api/[^"\']+)["\']',
            r'["\'](/[^"\']+\.php\?[^"\']*)["\']',
            r'fetch\(["\']([^"\']+)["\']',
            r'axios\.(?:get|post|put|delete)\(["\']([^"\']+)["\']',
            r'\.ajax\([^)]*url:\s*["\']([^"\']+)["\']'
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, html_content)
            endpoints.extend(matches)
        
        return list(set(endpoints))
