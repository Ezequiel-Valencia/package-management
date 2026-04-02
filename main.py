from packagemanagement.type.packages import PackageType
from packagemanagement.type.package_managers import PackageManagerEnum
from types import ModuleType
from packagemanagement.package_lists import app_work, cli_work
from packagemanagement.core import runner, config_all_packages, update_and_upgrade_all_packages
import argparse
import json
import sys
from packagemanagement.cli import main_function
from packagemanagement.config.globals import set_ordered_managers

def get_allowed_package_managers() -> dict[PackageType, list[PackageManagerEnum]]:
    _CONFIG_FILES = {
        "darwin": "config/mac_config.json",
        "linux":  "config/linux_config.json",
    }

    _config_file = _CONFIG_FILES.get(sys.platform)
    if _config_file is None:
        raise RuntimeError(f"Unsupported platform: {sys.platform}. Expected one of: {list(_CONFIG_FILES.keys())}")

    with open(_config_file) as f:
        _raw = json.load(f)

    return {
        PackageType[k]: [PackageManagerEnum[pm] for pm in v]
        for k, v in _raw.items()
    }


if __name__ == "__main__":
    ps_to_install: list[ModuleType] = [app_work, cli_work]
    main_function(allowed_for_each_type=get_allowed_package_managers(), ps_to_install=ps_to_install)

