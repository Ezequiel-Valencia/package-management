from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from packagemanagement.type.containers import HardwareResources, ContainerStack, ContainerType
import subprocess
import logging

logger = logging.getLogger(__name__)


class DockerStack(ContainerStack):

    def __init__(
        self,
        compose_file: Path,
        profile: HardwareResources = HardwareResources.CPU,
        override_files: list[Path] | None = None,
    ):
        self.compose_file = compose_file
        self.profile = profile
        self.override_files: list[Path] = override_files or []
        self.c_type = ContainerType.DOCKER

    def _base_cmd(self) -> str:
        parts = ["docker", "compose", "-f", str(self.compose_file)]
        for override in self.override_files:
            parts += ["-f", str(override)]
        parts += ["--profile", self.profile.value]
        return " ".join(parts)

    def pull_image_command(self) -> str:
        return f"{self._base_cmd()} pull"

    def start_command(self) -> str:
        return f"{self._base_cmd()} up -d"

    def stop_command(self) -> str:
        return f"{self._base_cmd()} down"

    def status_command(self) -> str:
        return f"{self._base_cmd()} ps"
    
    def configure(self):
        pass
    
