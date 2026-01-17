from packagemanagement.type.packages import CLIPackage
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
        hook = ''
        shell_file = ''
        home = pathlib.Path.home()
        if 'linux' in platform:
            hook = 'eval "$(direnv hook bash)"'
            shell_file = f'{home}/.bashrc'
        elif 'darwin' in platform:
            hook = 'eval "$(direnv hook zsh)"'
            shell_file = f'{home}/.zshrc'
        else:
            raise RuntimeError(f"Config not support for os {platform}")

        with open(shell_file, "r") as f:
            bash_content = f.read()
        
        if hook not in bash_content:
            with open(shell_file, "a+") as f:
                logger.info(f"Configuring {shell_file} for direnv hook.")
                shutil.copy(shell_file, f'{shell_file}_{datetime.datetime.now()}')
                f.write(f'\n{hook}\n')



#!----- Interesting ---------!#
# Easier curl for APIs, # https://github.com/httpie/cli
# https://github.com/Aider-AI/aider
# AWS Stack Mock locally https://github.com/localstack/localstack
# Docker container for any distro, https://github.com/89luca89/distrobox
# Ubuntu VM easy, https://github.com/canonical/multipass
# AI auto tab assistant, https://github.com/TabbyML/tabby
# Create CLI's, https://github.com/spf13/cobra
# Better git diff, https://github.com/dandavison/delta

