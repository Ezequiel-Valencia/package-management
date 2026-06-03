from packagemanagement.type.packages import PackageType
from packagemanagement.type.package_managers import PackageManagerEnum
from types import ModuleType
import importlib
from packagemanagement.core import runner, config_all_packages, update_and_upgrade_all_packages
import json
import sys
import platform
from packagemanagement.cli import main_function
from packagemanagement.config.globals import set_ordered_managers

_CONFIG_FILES = {
    "darwin": "config/mac_config.json",
    "linux":  "config/linux_config.json",
    "wsl": "config/wsl.json",
}

def _load_config() -> dict:
    system = sys.platform
    _config_file = _CONFIG_FILES[system]
    uname = platform.uname().release.lower()
    if system == 'linux' and 'microsoft' in uname and 'wsl' in uname:
        _config_file = _CONFIG_FILES['wsl']
    if _config_file is None:
        raise RuntimeError(f"Unsupported platform: {sys.platform}. Expected one of: {list(_CONFIG_FILES.keys())}")
    with open(_config_file) as f:
        return json.load(f)

def get_allowed_package_managers() -> dict[PackageType, list[PackageManagerEnum]]:
    _raw = _load_config()
    return {
        PackageType[k]: [PackageManagerEnum[pm] for pm in v]
        for k, v in _raw["package_managers"].items()
    }

def get_modules_to_install() -> list[ModuleType]:
    _raw = _load_config()
    return [
        importlib.import_module(name)
        for name in _raw["modules"]
    ]


if __name__ == "__main__":
    main_function(allowed_for_each_type=get_allowed_package_managers(), ps_to_install=get_modules_to_install())
