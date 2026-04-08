from packagemanagement.type.packages import CLIPackage
from packagemanagement.type.package_managers import PackageManagerEnum

# -----------------------------------------------------------------------
# Defensive / vulnerability-discovery security tools
# -----------------------------------------------------------------------
# All packages here are focused on *finding* vulnerabilities so they can
# be fixed — not exploitation.  Think: scanners, auditors, analyzers.
# -----------------------------------------------------------------------


# Network discovery & port scanning, https://nmap.org/
class Nmap(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "nmap",
            PackageManagerEnum.BREW: "nmap",
        }


# Web application vulnerability scanner, https://github.com/sullo/nikto
class Nikto(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "nikto",
            PackageManagerEnum.BREW: "nikto",
        }


# SSL/TLS configuration tester, https://github.com/drwetter/testssl.sh
class Testssl(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "testssl",
        }


# DNS enumeration & subdomain discovery, https://github.com/darkoperator/dnsrecon
class Dnsrecon(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "dnsrecon",
            PackageManagerEnum.BREW: "dnsrecon",
        }


# Open-source vulnerability scanner for containers & filesystems, https://github.com/anchore/grype
class Grype(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "grype",
        }


# SBOM (Software Bill of Materials) generator — pairs with Grype, https://github.com/anchore/syft
class Syft(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "syft",
        }


# Static secret / credential scanner for repos, https://github.com/gitleaks/gitleaks
class Gitleaks(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "gitleaks",
            PackageManagerEnum.BREW: "gitleaks",
        }


# Detect hardcoded secrets in source code, https://github.com/trufflesecurity/trufflehog
class Trufflehog(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "trufflehog",
        }


# Static analysis security testing for many languages (SAST), https://semgrep.dev/
class Semgrep(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "semgrep",
        }


# Dependency vulnerability audit for Python projects, https://pypi.org/project/pip-audit/
class PipAudit(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "pip-audit",
        }


# OSV-based dependency vulnerability scanner (multi-ecosystem), https://github.com/google/osv-scanner
class OsvScanner(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "osv-scanner",
        }


# CIS-benchmark / misconfiguration scanner for containers & IaC, https://github.com/aquasecurity/trivy
class Trivy(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "trivy",
            PackageManagerEnum.BREW: "trivy",
        }


# IaC security scanner (Terraform, CloudFormation, K8s, …), https://github.com/aquasecurity/tfsec
class Tfsec(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "tfsec",
        }


# Lightweight host-based intrusion detection / file integrity monitoring, https://github.com/Tripwire/tripwire-open-source
class Tripwire(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "tripwire",
        }


# Network traffic analysis & packet capture, https://www.wireshark.org/ (CLI component)
class Tshark(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "tshark",
            PackageManagerEnum.BREW: "wireshark",
        }


#!----- Interesting / future additions ---------!#
# OpenVAS / Greenbone — full-stack vulnerability management, https://www.greenbone.net/
# Lynis — security auditing for Unix/Linux systems, https://cisofy.com/lynis/
# Nuclei — fast, template-based vulnerability scanner, https://github.com/projectdiscovery/nuclei
# Checkov — IaC static analysis (Python-based), https://www.checkov.io/
# Dependency-check (OWASP) — Java/Node/Python SCA, https://owasp.org/www-project-dependency-check/
