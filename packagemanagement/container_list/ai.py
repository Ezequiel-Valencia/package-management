from pathlib import Path
from sys import platform
from logging import getLogger
import subprocess

from packagemanagement.type.packages import CLIPackage, GUIPackage
from packagemanagement.type.package_managers import PackageManagerEnum
from packagemanagement.type.containers import HardwareResources
from packagemanagement.type.container_manager import DockerStack

logger = getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[2]
_COMPOSE_FILE = _REPO_ROOT / "docker-compose.yml"
_COMPOSE_GPU_OVERRIDE = _REPO_ROOT / "docker-compose.gpu.yml"
_COMPOSE_CPU_OVERRIDE = _REPO_ROOT / "docker-compose.cpu.yml"


class AIDockerStack(DockerStack):
    """
    Orchestrates the local AI Docker Compose stack (Tabby, Ollama, Open WebUI).
    """

    def __init__(self, use_gpu: bool = False):
        profile = HardwareResources.GPU if use_gpu else HardwareResources.CPU
        override = _COMPOSE_GPU_OVERRIDE if use_gpu else _COMPOSE_CPU_OVERRIDE
        super().__init__(
            compose_file=_COMPOSE_FILE,
            profile=profile,
            override_files=[override]
        )
