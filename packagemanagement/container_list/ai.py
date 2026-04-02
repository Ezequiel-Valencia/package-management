from pathlib import Path
from sys import platform
from logging import getLogger
import subprocess

from packagemanagement.type.packages import CLIPackage, GUIPackage
from packagemanagement.type.package_managers import PackageManagerEnum
from packagemanagement.type.containers import HardwareResources
from packagemanagement.type.container_manager import DockerStack

logger = getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parents[0]
_COMPOSE_FILE = _REPO_ROOT / "ai_compose" / "docker-compose.yml"
_COMPOSE_GPU_OVERRIDE = _REPO_ROOT / "ai_compose" / "docker-compose.gpu.yml"
_COMPOSE_CPU_OVERRIDE = _REPO_ROOT / "ai_compose" / "docker-compose.cpu.yml"


def _has_nvidia_gpu() -> bool:
    try:
        subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


class AIDockerStack(DockerStack):
    """
    Orchestrates the local AI Docker Compose stack (Tabby, Ollama, Open WebUI).
    """

    def __init__(self):
        use_gpu = _has_nvidia_gpu()
        profile = HardwareResources.GPU if use_gpu else HardwareResources.CPU
        override = _COMPOSE_GPU_OVERRIDE if use_gpu else _COMPOSE_CPU_OVERRIDE
        super().__init__(
            compose_file=_COMPOSE_FILE,
            profile=profile,
            override_files=[override]
        )
    
    def configure(self):
        pull_code_model_command = ["docker", "exec", f"ollama", "ollama", "pull", "qwen2.5-coder:7b"]
        subprocess.run(
            pull_code_model_command,
            check=True
        )
        
