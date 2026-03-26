from enum import Enum
from sys import platform
import pathlib


class PackageType(Enum):
    GUI_APP = "gui_app"
    CLI = "cli"
    LIBRARY = "library"

class ShellType(Enum):
    BASH = "bash"
    ZSH = "zsh"

    def get_shell_type() -> "ShellType":
        if 'linux' in platform:
            return ShellType.BASH
        elif 'darwin' in platform:
            return ShellType.ZSH
        else:
            raise ValueError(f"Shell type for platform {platform} is not supported")

    def get_shell_hook_path(self) -> str:
        home = pathlib.Path.home()
        match self.value:
            case self.BASH.value:
                return f'{home}/.bashrc'
            case self.ZSH.value:
                return f'{home}/.zshrc'


# Package type should have it's own ranking for which manager
# Modules should themselves have a global preference
#

class Package:

    def __init__(self):
        self.package_dict: dict = {}
        self.p_type: PackageType
    
    def which_package_manager(self, ordered_managers: dict[PackageType, list['PackageManagerEnum']]) -> 'PackageManagerEnum':
        keys = self.package_dict.keys()
        my_managers = ordered_managers[self.p_type]
        if len(keys) == 1:
            for i in keys:
                return i
        else:
            for r in my_managers:
                if r in keys:
                    return r
            raise RuntimeError(f"No managers available {my_managers} could be found for package {self}")
    
    def get_package_name(self, manager: 'PackageManagerEnum') -> str:
        return self.package_dict[manager]

    def allow_sudo(self):
        return True
    
    def configure(self):
        pass


class GUIPackage(Package):
    p_type = PackageType.GUI_APP

class CLIPackage(Package):
    p_type = PackageType.CLI

class LibraryPackage(Package):
    p_type = PackageType.LIBRARY


