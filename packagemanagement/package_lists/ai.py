from packagemanagement.type.packages import CLIPackage
from packagemanagement.type.package_managers import PackageManagerEnum


# https://github.com/sst/opencode, CLI based code editor that is open source
class OpenCode(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "opencode"
        }

class ClaudCode(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "claude-code"
        }
        