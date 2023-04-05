"""
Functions to interact with obsidian.

example vault entry in obsidian configuration file:
"b6a07f524d21291c":{"path":"C:\\Users\\George\\OneDrive\\Documents\\Obsidian\\Personal","ts":1675369152995,"open":true}
"""

import os
import sys
import json


PLATFORM_IS_WINDOWS = sys.platform.startswith("win")


def find_obsidian_config_file_path():
    if PLATFORM_IS_WINDOWS:
        user = os.environ["HOMEPATH"]
        path = os.path.join(user, "AppData\\Roaming\\obsidian\\obsidian.json")
    else:
        raise Exception("non-windows platform not supported")
    if os.access(path, os.W_OK):
        return path
    else:
        return None


def get_vault_names():
    if not (path := find_obsidian_config_file_path()):
        return None
    with open(path, "r") as f:
        data = json.load(f)
        # data = json.loads(b"")  # for testing exception handling

    vaults = []
    for vault in data["vaults"].values():
        name = os.path.basename(vault["path"])
        vaults.append(name)
    return vaults


def open_vault_by_name(name):
    os.startfile("obsidian://open/?vault=" + name)


if __name__ == "__main__":  # testing
    print(get_vault_names())
