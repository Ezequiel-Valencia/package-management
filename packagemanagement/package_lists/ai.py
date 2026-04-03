from packagemanagement.type.packages import CLIPackage
from packagemanagement.type.package_managers import PackageManagerEnum
import json
import os
from pathlib import Path
from logging import getLogger

logger = getLogger(__name__)


# https://github.com/sst/opencode, CLI based code editor that is open source
class OpenCode(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "opencode"
        }

    def configure(self):
        config_dir = Path.home() / ".config" / "opencode"
        config_path = config_dir / "opencode.json"

        config_dir.mkdir(parents=True, exist_ok=True)

        config = {
            "$schema": "https://opencode.ai/config.json",
            "provider": {
                "ollama": {
                    "npm": "@ai-sdk/openai-compatible",
                    "name": "Ollama (Local)",
                    "options": {
                        "baseURL": "http://localhost:11434/v1"
                    },
                    "models": {
                        "mistral-small3.2": {
                            "name": "Local Mistral-Small 3.2",
                            "reasoning": False,
                            "tools": True
                        }
                    }
                }
            }
        }

        if config_path.exists():
            with open(config_path, "r") as f:
                existing = json.load(f)
            existing.setdefault("provider", {})["ollama"] = config["provider"]["ollama"]
            config = existing
            logger.info("Merged ollama provider into existing opencode config.")
        else:
            logger.info(f"Writing opencode config to {config_path}.")

        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)

class ClaudCode(CLIPackage):
    def __init__(self):
        self.package_dict: dict[PackageManagerEnum, str] = {
            PackageManagerEnum.BREW  : "claude-code"
        }
        