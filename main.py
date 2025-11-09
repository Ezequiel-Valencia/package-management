from packagemanagement.type.packages import PackageType, PackageManager
from types import ModuleType
from packagemanagement.package_lists import app_work, cli_work
from packagemanagement.core import runner



if __name__ == "__main__":
    allowed_for_each_type: dict[PackageType, list[PackageManager]] = {
        PackageType.GUI_APP: [PackageManager.FLATPAK, PackageManager.SNAP, PackageManager.APT, PackageManager.NIX],
        PackageType.CLI: [PackageManager.APT, PackageManager.SNAP, PackageManager.BREW],
        PackageType.LIBRARY: [PackageManager.APT, PackageManager.BREW]
    }
    ps_to_install: list[ModuleType] = [app_work, cli_work]
    runner(allowed_for_each_type, ps_to_install)






