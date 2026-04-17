import json
import pathlib

_STATE_FILE = pathlib.Path("installed_state.json")


def load_state() -> dict[str, dict]:
    if not _STATE_FILE.exists():
        return {}
    with open(_STATE_FILE) as f:
        return json.load(f)


def save_state(state: dict[str, dict]) -> None:
    with open(_STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def record_installed(class_name: str, manager_name: str, package_name: str) -> None:
    state = load_state()
    state[class_name] = {"manager": manager_name, "package_name": package_name}
    save_state(state)


def remove_from_state(class_name: str) -> None:
    state = load_state()
    if class_name in state:
        del state[class_name]
        save_state(state)
