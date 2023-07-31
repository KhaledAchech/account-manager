import platform
import subprocess
import json
import configparser
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
        cprint("File permissions set successfully.", THEME.get("success"))
    except subprocess.CalledProcessError as e:
        cprint(f"Error setting file permissions: {e}", THEME.get("error"))
        system('cls')
        exit(0)

def get_db_params() -> dict:
    config = configparser.ConfigParser()
    config.read(FILE_PATH)
    return {
        "host": config.get("Database", "host"),
        "database": config.get("Database", "database"),
        "default_database": config.get("Database", "default_database"),
        "user": config.get("Database", "user"),
        "password": config.get("Database", "password"),
        "port": config.get("Database", "port")
    }
