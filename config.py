import platform
import subprocess
import json
from os import system
from termcolor import cprint

# TO DO: Need to handle corner cases and refactor code
def get_constant_from_json(json_file: str = None, branch: str = None, key: str = None) -> str:
    with open(json_file, "r") as constants_file:
        constants = json.load(constants_file)
    if not key:
        return constants.get(branch)
    return constants.get(branch).get(key)

CONSTS_FILE = "constants.json"
FILE_PATH = get_constant_from_json(CONSTS_FILE, "files", "conifg_path")
MESSAGES = get_constant_from_json(CONSTS_FILE, "messages")
THEME = get_constant_from_json(CONSTS_FILE, "style", "theme")
INQUIRER = get_constant_from_json(CONSTS_FILE, "style", "inquirer")

def set_file_permissions() -> None:
    if platform.system() == "Windows":
        command = ["icacls", FILE_PATH, "/grant", f"*S-1-1-0:(R)"]
    else:
        command = ["chmod", "600", FILE_PATH]

    try:
        subprocess.run(command, check=True)
        cprint("File permissions set successfully.", "green")
    except subprocess.CalledProcessError as e:
        cprint(f"Error setting file permissions: {e}", "red")
        system('cls')
        exit(0)
