from packagemanagement.type.package_managers import PackageManagerEnum
from packagemanagement.type.packages import GUIPackage


class VSCodium(GUIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.NIX : "nixpkgs.vscodium",
            PackageManagerEnum.BREW: "vscodium"
        }

# class Lens(Package):
#     package_dict: dict[PackageManagerEnum, str] = {
#         PackageManagerEnum.NIX : "nixpkgs.lens"
#     }

class Gitkraken(GUIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.FLATPAK : "com.axosoft.GitKraken",
            PackageManagerEnum.BREW: "gitkraken"
        }

class IntelliJ(GUIPackage):

    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.FLATPAK : "com.jetbrains.IntelliJ-IDEA-Community",
            PackageManagerEnum.BREW: "intellij-idea"
        }


class Ghostty(GUIPackage):

    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.SNAP_CLASSIC : "ghostty",
            PackageManagerEnum.BREW: "ghostty"
        }

    def configure(self):
        # So that when ssh into various nodes, the XTerm is known
        inserted_into_bash = """
        if [[ "$TERM_PROGRAM" == "ghostty" ]]; then
            export TERM=xterm-256color
        fi"""


#!----- Interesting ---------!#
# Remote IDE tool, https://github.com/loft-sh/devpod
# Wordpress for backend admin panels, https://github.com/appsmithorg/appsmith?tab=readme-ov-file
# React framework close to no-code, https://github.com/refinedev/refine
# API Interactive GUI, https://github.com/hoppscotch/hoppscotch

