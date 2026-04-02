from enum import Enum
from abc import ABC, abstractmethod


class ContainerType(Enum):
    DOCKER = "docker"

class HardwareResources(Enum):
    GPU = "gpu"
    CPU = "cpu"

class ContainerStack(ABC):
    c_type: ContainerType

    @abstractmethod
    def pull_image_command(self):
        pass

    @abstractmethod
    def start_command(self):
        pass

    @abstractmethod
    def stop_command(self):
        pass

    @abstractmethod
    def status_command(self):
        pass

