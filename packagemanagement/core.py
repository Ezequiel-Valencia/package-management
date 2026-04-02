import subprocess
import inspect

from packagemanagement.config.globals import set_ordered_managers, get_ordered_managers
from typing import IO
from types import ModuleType
from packagemanagement.type.packages import Package, PackageType
from packagemanagement.type.package_managers import PackageManagerEnum, PackageManager
from packagemanagement.type.containers import ContainerStack
from getpass import getpass
from logging import getLogger

logger = getLogger(__name__)


def install_packages(
    p_list: list[Package], passwd: str, er_log: IO, inf_log: IO, change_log: IO
):
    ordered_managers = get_ordered_managers()
    for package in p_list:
        pref: PackageManagerEnum = package.which_package_manager(
            ordered_managers=ordered_managers
        )
        check_command = pref.value.get_check_command(package)
        result = subprocess.run(check_command, shell=True, capture_output=True)
        package_name = package.get_package_name(pref)
        if result.stdout != b"":
            logger.info(
                f"==== {package_name} seems to already be installed with manager {pref}. ==="
            )
        elif result.stderr != b"":
            raise RuntimeError(
                f"Error checking package {package_name} when using manager {pref}: {result.stderr}"
            )
        else:
            command = pref.value.get_install_command(package)
            kwargs = {
                "args": command,
                "check": True,
                "stderr": er_log,
                "stdout": inf_log,
            }

            sudo_required_pm = {PackageManagerEnum.APT, PackageManagerEnum.SNAP}
            if package.allow_sudo() and pref in sudo_required_pm:
                kwargs["args"] = "sudo -S " + command
                kwargs["input"] = passwd

            logger.info(subprocess.run(**kwargs, shell=True, text=True))
            package.configure()
            change_log.write(f"{package_name} was installed using {pref}")

def config_all_packages(modules_with_packages: list[Package]) -> None:
    for m in modules_with_packages:
        packs = list_packages_to_install(m)
        for p in packs:
            p.configure()


def update_and_upgrade_all_packages() -> None:
    ordered_managers: dict[PackageType, list[PackageManagerEnum]] = (
        get_ordered_managers()
    )
    password = getpass("Sudo Password: ")
    with open("err.log", "w+") as err_log:
        with open("info.log", "w+") as info_log:
            kwargs = {"args": "", "check": True, "stderr": err_log, "stdout": info_log, "input": password}
            already_updated = set()
            for list_of_pack_enums in ordered_managers.values():
                for pm in list_of_pack_enums:
                    if pm not in already_updated:
                        kwargs["args"] = pm.value.get_update_command()
                        logger.info(subprocess.run(**kwargs, shell=True, text=True))
                        kwargs["args"] = pm.value.get_upgrade_command()
                        logger.info(subprocess.run(**kwargs, shell=True, text=True))
                        logger.info(
                            f"=== Update and upgraded all packages for manager: {pm.name} ==="
                        )
                        already_updated.add(pm)


def list_packages_to_install(mod: ModuleType) -> list[Package]:
    # Iterate through all classes defined in the module
    ps = []
    for name, obj in inspect.getmembers(mod, inspect.isclass):
        # Check if the class is defined in this module (not imported)
        if obj.__module__ == mod.__name__:
            # Check if it’s a subclass of MyBaseClass (but not the base itself)
            if issubclass(obj, Package) and obj is not Package:
                ps.append(obj())
    return ps


def get_container_stack(mod: ModuleType) -> ContainerStack:
    for name, obj in inspect.getmembers(mod, inspect.isclass):
        if obj.__module__ == mod.__name__:
            if issubclass(obj, ContainerStack) and obj is not Package:
                return obj()
    raise RuntimeError(f"Expected a class which inherited 'ContainerStack' from: {mod}")


def runner(
    allowed_managers_for_each_type: dict[PackageType, list[PackageManagerEnum]],
    modules_with_packages: list[ModuleType],
):
    set_ordered_managers(ordered_managers=allowed_managers_for_each_type)
    password = getpass("Sudo Password: ")

    with open("err.log", "w+") as err_log:
        with open("info.log", "w+") as info_log:
            with open("change.log", "w+") as change_log:
                for m in modules_with_packages:
                    packs = list_packages_to_install(m)
                    install_packages(
                        packs,
                        er_log=err_log,
                        inf_log=info_log,
                        passwd=password,
                        change_log=change_log,
                    )
                

def container_runner(modules_with_container_stacks: list[ModuleType], container_state: str):
    for stack in modules_with_container_stacks:
        c_stack = get_container_stack(stack)
        match container_state:
            case "start":
                command_to_run = c_stack.start_command().split(" ")
            case "stop":
                command_to_run = c_stack.stop_command().split(" ")
            case "status":
                command_to_run = c_stack.status_command().split(" ")
            case _:
                raise ValueError(f"Expected command of either start, stop, or status. Instead got {container_state}")
        logger.info(f"Running {command_to_run}")
        subprocess.run(command_to_run, check=True)
        logger.info(f"Finished running {command_to_run}")
        if container_state == "start":
            c_stack.configure()
            logger.info("Finished configuring container stack.")
     
