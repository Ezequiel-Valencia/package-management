from packagemanagement.type.packages import PackageType
from packagemanagement.type.package_managers import PackageManagerEnum
from types import ModuleType
from packagemanagement.package_lists import app_work, cli_work
from packagemanagement.core import runner, config_all_packages, update_and_upgrade_all_packages
import argparse
from packagemanagement.config.globals import set_ordered_managers


def main_function(allowed_for_each_type: dict[PackageType, list[PackageManagerEnum]],
                    ps_to_install: list[ModuleType]):
    parser = argparse.ArgumentParser(description="Personal Package Management")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("install", help="Install all packages.")
    subparsers.add_parser("update", help="Update all packages.")
    subparsers.add_parser("configure", help="Configure all packages.")

    args = parser.parse_args()
    set_ordered_managers(allowed_for_each_type)
    
    if args.command == "install":
        runner(allowed_for_each_type, ps_to_install)
    elif args.command == "update":
        update_and_upgrade_all_packages()
    elif args.command == "configure":
        config_all_packages(ps_to_install)
    else:
        raise RuntimeError("Expected command to be given, options are: [install, update, configure].")
