import re
import json
import logging
from urllib.parse import urlparse, parse_qs, urlencode

class VulnerabilityScanner:
    def __init__(self, session):
        self.session = session
        self.logger = logging.getLogger(__name__)
        
    def scan_sql_injection(self, url):
        sql_payloads = [
            "'",
            "\"",
            "' OR '1'='1",
            "' AND 1=1--",
            "' UNION SELECT NULL--",
            "' AND SLEEP(5)--",
            "'; WAITFOR DELAY '00:00:05'--"
        ]
        
        parsed = urlparse(url)
        query_params = parse_qs(parsed.query)
        
        for param in query_params.keys():
            for payload in sql_payloads:
                # Test each parameter with SQL payloads
                test_params = query_params.copy()
                test_params[param] = [payload]
                
                new_query = urlencode(test_params, doseq=True)
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"
                
                try:
                    response = self.session.get(test_url)
                    
                    # Check for SQL errors
                    sql_errors = [
                        "SQL syntax",
                        "mysql_fetch",
                        "ORA-",
                        "PostgreSQL",
                        "SQLite",
                        "SQL Server",
                        "ODBC",
                        "JDBC",
                        "Syntax error"
                    ]
                    
                    for error in sql_errors:
                        if error.lower() in response.text.lower():
                            self.logger.critical(f"SQL Injection found: {test_url}")
                            break
                            
                except Exception as e:
                    self.logger.error(f"Error scanning {test_url}: {e}")
