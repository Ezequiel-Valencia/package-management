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


class NixPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.NIX)
        return f"nix-env -iA {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.NIX)
        return f"nix-env --query --installed | grep {package_name.split('.')[1]}"  # This is because pacs are formatted nix.{actual name}

class APTPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.APT)
        return f"apt-get install -y {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.APT)
        return f"dpkg -l | grep {package_name}"

class SnapPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP)
        return f"snap install {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP)
        return f"snap list | grep {package_name}"

class FlatPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.FLATPAK)
        return f"flatpak install -y {package_name}"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.FLATPAK)
        return f"flatpak list | grep {package_name}"

class SnapClassicPackageManager(PackageManager):
    def get_install_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP_CLASSIC)
        return f"snap install {package_name} --classic"

    def get_check_command(self, package: "Package") -> str:
        package_name = package.get_package_name(PackageManagerEnum.SNAP_CLASSIC)
        return f"snap list | grep {package_name}"

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

class PackageManagerEnum(Enum):
    NIX = NixPackageManager()
    APT = APTPackageManager()
    SNAP = SnapPackageManager()
    FLATPAK = FlatPackageManager()
    SNAP_CLASSIC = SnapClassicPackageManager()
    BREW = BrewPackageManager()


class RankedManager:
    package_manager: PackageManager
    ranking: dict[PackageType, int]

    def __init__(self, manager: PackageManager, ranking: dict[PackageType, int]):
        self.package_manager = manager
        self.ranking = ranking
