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
            PackageManagerEnum.BREW: "nmap",
            PackageManagerEnum.PACMAN: "nmap",
        }


# Web application vulnerability scanner, https://github.com/sullo/nikto
class Nikto(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "nikto",
            PackageManagerEnum.PACMAN: "nikto",
        }


# DNS enumeration & subdomain discovery, https://github.com/darkoperator/dnsrecon
class Dnsrecon(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.PIPX: "dnsrecon",
            PackageManagerEnum.PACMAN: "dnsrecon",
        }


# Open-source vulnerability scanner for containers & filesystems, https://github.com/anchore/grype
class Grype(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "grype",
            PackageManagerEnum.PACMAN: "grype",
        }


# SBOM (Software Bill of Materials) generator — pairs with Grype, https://github.com/anchore/syft
class Syft(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "syft",
            PackageManagerEnum.PACMAN: "syft",
        }


# Static secret / credential scanner for repos, https://github.com/gitleaks/gitleaks
class Gitleaks(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "gitleaks",
            PackageManagerEnum.PACMAN: "gitleaks",
        }


# Detect hardcoded secrets in source code, https://github.com/trufflesecurity/trufflehog
class Trufflehog(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "trufflehog",
            PackageManagerEnum.PACMAN: "trufflehog",
        }


# OSV-based dependency vulnerability scanner (multi-ecosystem), https://github.com/google/osv-scanner
class OsvScanner(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "osv-scanner",
            PackageManagerEnum.PACMAN: "osv-scanner",
        }


# CIS-benchmark / misconfiguration scanner for containers & IaC, https://github.com/aquasecurity/trivy
class Trivy(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "trivy",
            PackageManagerEnum.PACMAN: "trivy",
        }


# Network traffic analysis & packet capture, https://www.wireshark.org/ (CLI component)
class WireShark(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "wireshark",
            PackageManagerEnum.PACMAN: "wireshark-qt",
        }

# Lynis — security auditing for Unix/Linux systems,
class Lynis(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "lynis",
            PackageManagerEnum.PACMAN: "lynis",
        }

# Nuclei — fast, template-based vulnerability scanner, https://github.com/projectdiscovery/nuclei    
class Nuclei(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW: "nuclei",
            PackageManagerEnum.PACMAN: "nuclei",
        }

# Figure out what kind of firewall a website might have
class WafWoof(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.PIPX: "wafw00f",
            PackageManagerEnum.PACMAN: "wafw00f",
        }

# Word Press Scanner
# class WPScan(CLIPackage):
#     def __init__(self):
#         self.package_dict: dict[PackageManagerEnum, str] = {
#             PackageManagerEnum.BREW: "wpscanteam/tap/wpscan"
#         }

#!----- Interesting / future additions ---------!#
# OpenVAS / Greenbone — full-stack vulnerability management, https://www.greenbone.net/
# Checkov — IaC static analysis (Python-based), https://www.checkov.io/
# Dependency-check (OWASP) — Java/Node/Python SCA, https://owasp.org/www-project-dependency-check/
# Nikto - Web server scanner, https://github.com/sullo/nikto
# What web - Web server scanner, https://github.com/urbanadventurer/WhatWeb
