from abc import ABC, abstractmethod
from enum import Enum

from packagemanagement.type.packages import PackageType, GUIPackage, Package


class PackageManager(ABC):
    @abstractmethod
    def get_install_command(self, package: "Package") -> str:
        pass

    @abstractmethod
    def get_check_command(self, package: "Package") -> str:
        pass

    @abstractmethod
    def get_update_command(self) -> str:
        pass

    @abstractmethod
    def get_upgrade_command(self) -> str:
        pass


class NixPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.NIX)
        return f"nix-env -iA {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.NIX)
        return f"nix-env --query --installed | grep {package_name.split('.')[1]}"  # This is because pacs are formatted nix.{actual name}

    def get_update_command(self) -> str:
        return "echo 'Hello World.'"

    def get_upgrade_command(self) -> str:
        return "echo 'Hello World'"


class APTPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.APT)
        return f"apt-get install -y {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.APT)
        return f"dpkg -l | grep {package_name}"

    def get_update_command(self) -> str:
        return "sudo apt-get update"

    def get_upgrade_command(self) -> str:
        return "sudo apt-get upgrade -y"


class SnapPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP)
        return f"snap install {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP)
        return f"snap list | grep {package_name}"

    def get_update_command(self) -> str:
        return "sudo snap refresh"

    def get_upgrade_command(self) -> str:
        return "sudo snap refresh"


class FlatPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.FLATPAK)
        return f"flatpak install -y {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.FLATPAK)
        return f"flatpak list | grep {package_name}"

    def get_update_command(self) -> str:
        return "flatpak update -y"

    def get_upgrade_command(self) -> str:
        return "flatpak upgrade -y"


class SnapClassicPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP_CLASSIC)
        return f"snap install {package_name} --classic"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP_CLASSIC)
        return f"snap list | grep {package_name}"

    def get_update_command(self) -> str:
        return "sudo snap refresh"

    def get_upgrade_command(self) -> str:
        return "sudo snap refresh"


class BrewPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.BREW)
        args = ""
        if isinstance(package, GUIPackage):
            args += "--cask "
        return f"brew install {args}{package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.BREW)
        return f"brew list | grep {package_name}"

    def get_update_command(self) -> str:
        return "brew update"

    def get_upgrade_command(self) -> str:
        return "brew upgrade"

class PipxPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.PIPX)
        return f"pipx install {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.PIPX)
        return f"pipx list | grep {package_name}"

    def get_update_command(self) -> str:
        return "echo 'Hello.'"

    def get_upgrade_command(self) -> str:
        return "pipx upgrade-all"


class PackageManagerEnum(Enum):
    NIX = NixPackageManager()
    APT = APTPackageManager()
    SNAP = SnapPackageManager()
    FLATPAK = FlatPackageManager()
    SNAP_CLASSIC = SnapClassicPackageManager()
    BREW = BrewPackageManager()
    PIPX = PipxPackageManager()


class RankedManager:
    package_manager: PackageManager
    ranking: dict[PackageType, int]

    def __init__(self, manager: PackageManager, ranking: dict[PackageType, int]):
        self.package_manager = manager
        self.ranking = ranking
