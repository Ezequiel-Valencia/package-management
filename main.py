from packagemanagement.type.packages import PackageType
from packagemanagement.type.package_managers import PackageManagerEnum
from types import ModuleType
from packagemanagement.package_lists import app_work, cli_work
from packagemanagement.core import runner, config_all_packages
import argparse

allowed_for_each_type: dict[PackageType, list[PackageManagerEnum]] = {
    PackageType.GUI_APP: [PackageManagerEnum.FLATPAK, PackageManagerEnum.SNAP, PackageManagerEnum.SNAP_CLASSIC, PackageManagerEnum.APT, PackageManagerEnum.NIX],
    PackageType.CLI: [PackageManagerEnum.APT, PackageManagerEnum.SNAP, PackageManagerEnum.SNAP_CLASSIC, PackageManagerEnum.BREW],
    PackageType.LIBRARY: [PackageManagerEnum.APT, PackageManagerEnum.BREW]
}



def main_function():
    parser = argparse.ArgumentParser(description="Personal Package Management")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("install", help="Install all packages.")
    subparsers.add_parser("update", help="Update all packages.")
    subparsers.add_parser("configure", help="Configure all packages.")

    args = parser.parse_args()
    ps_to_install: list[ModuleType] = [app_work, cli_work]
    
    if args.command == "install":
        runner(allowed_for_each_type, ps_to_install)
    elif args.command == "update":
        pass
    elif args.command == "configure":
        config_all_packages(ps_to_install)
    else:
        raise RuntimeError("Expected command to be given, options are: [install, update, configure].")


if __name__ == "__main__":
    main_function()

