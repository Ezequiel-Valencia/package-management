from packagemanagement.type.packages import PackageType
from packagemanagement.type.package_managers import PackageManagerEnum
from types import ModuleType
from packagemanagement.package_lists import app_work, cli_work
from packagemanagement.core import runner



if __name__ == "__main__":
    allowed_for_each_type: dict[PackageType, list[PackageManager]] = {
        PackageType.GUI_APP: [PackageManagerEnum.FLATPAK, PackageManagerEnum.SNAP, PackageManagerEnum.SNAP_CLASSIC, PackageManagerEnum.APT, PackageManagerEnum.NIX],
        PackageType.CLI: [PackageManagerEnum.APT, PackageManagerEnum.SNAP, PackageManagerEnum.SNAP_CLASSIC, PackageManagerEnum.BREW],
        PackageType.LIBRARY: [PackageManagerEnum.APT, PackageManagerEnum.BREW]
    }
    ps_to_install: list[ModuleType] = [app_work, cli_work]
    runner(allowed_for_each_type, ps_to_install)






