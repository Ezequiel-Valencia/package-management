from packagemanagement.type.packages import CLIPackage, ShellType
from packagemanagement.type.package_managers import PackageManagerEnum
from sys import platform
import shutil
import datetime
import pathlib
from logging import getLogger
import subprocess
import os
from pathlib import Path

logger = getLogger(__name__)

class Htop(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "htop",
            PackageManagerEnum.BREW: "htop"
        }

class Bat(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "bat",
            PackageManagerEnum.BREW: "bat"
        }

# Fuzzy find in terminal, https://github.com/junegunn/fzf
class Fzf(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "fzf",
            PackageManagerEnum.BREW: "fzf"
        }

# Better ls, https://github.com/eza-community/eza
class Eza(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW : "eza"
        }

# Better du, https://github.com/bootandy/dust
class DuDust(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW : "dust"
        }

# Better df, https://github.com/muesli/duf
class Duf(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "duf",
            PackageManagerEnum.BREW: "duf"
        }

# Better find, https://github.com/sharkdp/fd
class FdFind(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.APT : "fd-find",
            PackageManagerEnum.BREW: "fd"
        }

# Better grep, https://github.com/BurntSushi/ripgrep
class Ripgrep(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW : "ripgrep"
        }

# Better man pages, https://github.com/tldr-pages/tldr
class Tldr(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW : "tlrc"
        }

class Yq(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.SNAP : "yq",
            PackageManagerEnum.BREW: "yq"
        }

# https://github.com/sst/opencode, CLI based code editor that is open source
class OpenCode(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "opencode"
        }
        
class Sops(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "sops"
        }

class Age(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "age"
        }

class NeoVim(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW : "neovim"
        }

    def configure(self):
        config_to_clone = "https://github.com/Ezequiel-Valencia/LazyVimStarter.git"
        neo_vim_config_dir = os.path.join(Path.home(), ".config", "nvim")

        # Clean slate every time following git instead
        if Path(neo_vim_config_dir).exists():
            shutil.rmtree(neo_vim_config_dir)
        os.mkdir(neo_vim_config_dir)
        subprocess.run(
            ['git', 'clone', config_to_clone, neo_vim_config_dir]
        )


class DirEnv(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "direnv",
            PackageManagerEnum.APT: "direnv"
        }
    
    def configure(self):
        shell_type = ShellType.get_shell_type()
        if shell_type == ShellType.BASH or shell_type == shell_type.ZSH:
            hook = f'eval "$(direnv hook {shell_type.value})"'
            _add_line_to_shell_hook(line_to_add=hook, package_name="DirEnv", shell_type=shell_type)
        else:
            raise ValueError("Only supports bash or zsh for now.")


class Starship(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "starship"
        }
    
    def configure(self):
        shell_type: ShellType = ShellType.get_shell_type()
        if shell_type == ShellType.BASH or shell_type == ShellType.ZSH:
            hook = f'eval "$(starship init {shell_type.value})"'
            _add_line_to_shell_hook(line_to_add=hook, package_name="starship", shell_type=shell_type)
        else:
            raise ValueError("Only supports bash or zsh for now.")



def _add_line_to_shell_hook(line_to_add: str, package_name: str, shell_type: ShellType):
    shell_hook_file = shell_type.get_shell_hook_path()
    with open(shell_hook_file, "r") as f:
        bash_content = f.read()
    
    if line_to_add not in bash_content:
        with open(shell_hook_file, "a+") as f:
            logger.info(f"Configuring {shell_hook_file} for {package_name} hook.")
            shutil.copy(shell_hook_file, f'{shell_hook_file}_{datetime.datetime.now()}')
            f.write(f'\n{line_to_add}\n')
    else:
        logger.info(f" {package_name} has already been configured. ")    


# For when I do Tmux: https://youtu.be/jcrE1qrm_e8?si=N85YvBCLy-odLRSY




#!----- Interesting ---------!#
# Easier curl for APIs, # https://github.com/httpie/cli
# https://github.com/Aider-AI/aider
# AWS Stack Mock locally https://github.com/localstack/localstack
# Docker container for any distro, https://github.com/89luca89/distrobox
# Ubuntu VM easy, https://github.com/canonical/multipass
# AI auto tab assistant, https://github.com/TabbyML/tabby
# Create CLI's, https://github.com/spf13/cobra
# Better git diff, https://github.com/dandavison/delta

