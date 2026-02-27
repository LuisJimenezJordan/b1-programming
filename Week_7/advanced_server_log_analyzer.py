import re
import logging
from collections import defaultdict, Counter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('analysis_audit.log'),
        logging.StreamHandler()
    ]
)

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        # Updated pattern to capture referrer and user agent
        self.log_pattern = re.compile(
            r'(\S+) - - \[(.*?)\] "(\S+) (\S+) \S+" (\d+) (\d+) "([^"]*)" "([^"]*)"'
        )
        # Statistics
        self.total_requests = 0
        self.unique_ips = set()
        self.http_methods = Counter()
        self.urls = Counter()
        self.status_codes = Counter()
        self.errors = []

        # Security tracking
        self.failed_logins = defaultdict(list)
        self.forbidden_access = []
        self.security_incidents = []
        self.brute_force_detected = set()  # Track IPs already flagged

    def parse_log_line(self, line):
        """Parse a single log line."""
        match = self.log_pattern.match(line)
        if not match:
            return None

        ip, timestamp, method, url, status, size, referrer, user_agent = match.groups()
        return {
            'ip': ip,
            'timestamp': timestamp,
            'method': method,
            'url': url,
            'status': int(status),
            'size': int(size),
            'referrer': referrer,
            'user_agent': user_agent
        }

    def analyze_security(self, entry):
        """Analyze log entry for security issues."""

        # Track failed login attempts
        if entry['url'] == '/login' and entry['status'] == 401:
            self.failed_logins[entry['ip']].append(entry['timestamp'])
            
            # Only log once when threshold is reached (exactly 3 attempts)
            if len(self.failed_logins[entry['ip']]) == 3 and entry['ip'] not in self.brute_force_detected:
                incident = (
                    f"Brute force attempt from {entry['ip']} - "
                    f"{len(self.failed_logins[entry['ip']])} failed attempts"
                )
                self.security_incidents.append(incident)
                self.brute_force_detected.add(entry['ip'])
                logging.warning(incident)
            # Continue tracking if more attempts occur
            elif len(self.failed_logins[entry['ip']]) > 3 and entry['ip'] in self.brute_force_detected:
                # Update the incident count silently
                pass

        # Track forbidden access
        if entry['status'] == 403:
            incident = (
                f"Forbidden access attempt: {entry['ip']} -> {entry['url']}"
            )
            self.forbidden_access.append(incident)
            self.security_incidents.append(incident)
            logging.warning(incident)

        # Check for SQL injection patterns
        sql_patterns = ['union', 'select', 'drop', 'insert', '--', ';']
        url_lower = entry['url'].lower()
        if any(pattern in url_lower for pattern in sql_patterns):
            incident = (
                f"Potential SQL injection: {entry['ip']} -> {entry['url']}"
            )
            self.security_incidents.append(incident)
            logging.warning(incident)

        # Check for suspicious user agents
        suspicious_agents = ['sqlmap', 'nikto', 'nmap', 'masscan', 'metasploit', 'burp', 'scanner']
        user_agent_lower = entry['user_agent'].lower()
        if any(agent in user_agent_lower for agent in suspicious_agents):
            incident = (
                f"Suspicious user agent detected: {entry['ip']} - {entry['user_agent']}"
            )
            self.security_incidents.append(incident)
            logging.warning(incident)

        # Check for unusual HTTP methods
        standard_methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'OPTIONS', 'PATCH']
        if entry['method'] not in standard_methods:
            incident = (
                f"Unusual HTTP method: {entry['method']} from {entry['ip']} to {entry['url']}"
            )
            self.security_incidents.append(incident)
            logging.warning(incident)

    def process_logs(self):
        """Process the log file."""
        try:
            logging.info(f"Starting analysis of {self.log_file}")

            with open(self.log_file, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        entry = self.parse_log_line(line.strip())
                        if not entry:
                            logging.debug(f"Line {line_num}: Could not parse")
                            continue

                        # Update statistics
                        self.total_requests += 1
                        self.unique_ips.add(entry['ip'])
                        self.http_methods[entry['method']] += 1
                        self.urls[entry['url']] += 1
                        self.status_codes[entry['status']] += 1

                        # Track errors (4xx and 5xx)
                        if entry['status'] >= 400:
                            self.errors.append(entry)

                        # Security analysis
                        self.analyze_security(entry)

                    except Exception as e:
                        logging.error(f"Line {line_num}: Error processing - {e}")
                        continue

            logging.info(f"Analysis complete: {self.total_requests} requests processed")

        except FileNotFoundError:
            logging.error(f"Log file '{self.log_file}' not found")
            raise
        except PermissionError:
            logging.error(f"Permission denied reading '{self.log_file}'")
            raise

    def generate_summary_report(self):
        """Generate summary report."""
        try:
            with open('summary_report.txt', 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("SERVER LOG ANALYSIS SUMMARY\n")
                f.write("=" * 70 + "\n\n")
                f.write("TRAFFIC STATISTICS\n")
                f.write("-" * 70 + "\n")
                f.write(f"Total Requests: {self.total_requests}\n")
                f.write(f"Unique Visitors: {len(self.unique_ips)}\n\n")

                f.write("HTTP Methods:\n")
                for method, count in self.http_methods.most_common():
                    f.write(f"  {method}: {count}\n")

                f.write("\nMost Requested URLs:\n")
                for url, count in self.urls.most_common(5):
                    f.write(f"  {url}: {count} requests\n")

                f.write("\nStatus Code Distribution:\n")
                for status, count in sorted(self.status_codes.items()):
                    f.write(f"  {status}: {count}\n")

                f.write("\n" + "=" * 70 + "\n")
            logging.info("Summary report generated")
        except PermissionError:
            logging.error("Cannot write summary_report.txt")

    def generate_security_report(self):
        """Generate security incidents report."""
        try:
            with open('security_incidents.txt', 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("SECURITY INCIDENTS REPORT\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"Total Security Incidents: {len(self.security_incidents)}\n\n")

                f.write("BRUTE FORCE ATTEMPTS\n")
                f.write("-" * 70 + "\n")
                brute_force_count = 0
                for ip, attempts in self.failed_logins.items():
                    if len(attempts) >= 3:
                        f.write(f"IP: {ip} - {len(attempts)} failed login attempts\n")
                        brute_force_count += 1
                if brute_force_count == 0:
                    f.write("No brute force attempts detected.\n")

                f.write("\nFORBIDDEN ACCESS ATTEMPTS\n")
                f.write("-" * 70 + "\n")
                if self.forbidden_access:
                    for incident in self.forbidden_access:
                        f.write(f"{incident}\n")
                else:
                    f.write("No forbidden access attempts detected.\n")

                f.write("\nALL SECURITY INCIDENTS\n")
                f.write("-" * 70 + "\n")
                if self.security_incidents:
                    for incident in self.security_incidents:
                        f.write(f"{incident}\n")
                else:
                    f.write("No security incidents detected.\n")

                f.write("\n" + "=" * 70 + "\n")

            logging.info("Security report generated")

        except PermissionError:
            logging.error("Cannot write security_incidents.txt")

    def generate_error_log(self):
        """Generate error log."""
        try:
            with open('error_log.txt', 'w') as f:
                f.write("=" * 70 + "\n")
                f.write("HTTP ERRORS LOG (4xx and 5xx Status Codes)\n")
                f.write("=" * 70 + "\n\n")

                f.write(f"Total Errors: {len(self.errors)}\n\n")

                if self.errors:
                    for error in self.errors:
                        f.write(
                            f"[{error['timestamp']}] {error['ip']} - "
                            f"{error['method']} {error['url']} - "
                            f"Status: {error['status']}\n"
                        )
                else:
                    f.write("No errors detected.\n")

                f.write("\n" + "=" * 70 + "\n")

            logging.info("Error log generated")

        except PermissionError:
            logging.error("Cannot write error_log.txt")

def main():
    """Main function to run the log analyzer."""
    analyzer = LogAnalyzer('server.log')
    try:
        analyzer.process_logs()
        analyzer.generate_summary_report()
        analyzer.generate_security_report()
        analyzer.generate_error_log()

        print("\nAnalysis Complete!")
        print(f"Total requests: {analyzer.total_requests}")
        print(f"Security incidents: {len(analyzer.security_incidents)}")
        print(f"Errors found: {len(analyzer.errors)}")
        print("\nReports generated:")
        print("  - summary_report.txt")
        print("  - security_incidents.txt")
        print("  - error_log.txt")
        print("  - analysis_audit.log")
    except Exception as e:
        logging.critical(f"Analysis failed: {e}")
        print(f"Error: Analysis failed - {e}")

if __name__ == "__main__":
    main()