import platform
import subprocess
import json
import configparser
import base64

from os import system, getcwd, path, makedirs
from termcolor import cprint

from validation import assert_config


def get_constant_from_json(json_file: str = None, branch: str = None, key: str = None) -> str:
    with open(json_file, "r") as constants_file:
        constants = json.load(constants_file)
    if not key:
        return constants.get(branch)
    return constants.get(branch).get(key)


CONSTS_FILE = "constants.json"
API = get_constant_from_json(CONSTS_FILE, "external_service", "API")
DOMAINES = get_constant_from_json(CONSTS_FILE, "external_service", "domaines")
ONE_SEC_URL = get_constant_from_json(
    CONSTS_FILE, "external_service", "1sec_url")
FILE_PATH = get_constant_from_json(CONSTS_FILE, "files", "conifg_path")
ACTIONS = get_constant_from_json(CONSTS_FILE, "actions")
MESSAGES = get_constant_from_json(CONSTS_FILE, "messages")
THEME = get_constant_from_json(CONSTS_FILE, "style", "theme")
INQUIRER = get_constant_from_json(CONSTS_FILE, "style", "inquirer")
MAX_CHARS = 40

# Set the config.ini file permissions to only be granted to the system owner (not for all users).
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

def read_fernet_key():
    config = read_config()
    if config.has_section("Security") and config.has_option("Security", "fernet_key"):
        return config.get("Security", "fernet_key")
    return None

def read_config() -> object:
    config = configparser.ConfigParser()
    config.read(FILE_PATH)
    return config

def write_config(section: str, option: str = None, value: str = None) -> None:
    ''' config.ini only holds string configuration data. '''
    assert_config(section, option, value)

    config = read_config()
    if section not in config:
        config.add_section(section)

    config.set(section, option, value)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def get_db_params() -> dict:
    config = read_config()
    return {
        "host": config.get("Database", "host"),
        "database": config.get("Database", "database"),
        "default_database": config.get("Database", "default_database"),
        "user": config.get("Database", "user"),
        "password": config.get("Database", "password"),
        "port": config.get("Database", "port")
    }

def fetch_master_password() -> bytes:
    config = read_config()
    mp = config.get("Other", "master_password")
    return base64.b64decode(mp)

# Clean up a messy string into a list of strings aka a paragraph lines
def wrap_string(s: str) -> list:
    if len(s) <= MAX_CHARS:
        return [s]

    lines = []
    while len(s) > MAX_CHARS:
        wrap_index = s.rfind(' ', 0, MAX_CHARS)
        if wrap_index == -1:
            wrap_index = MAX_CHARS

        lines.append(s[:wrap_index])
        s = s[wrap_index:].strip()

    if s:
        lines.append(s)

    return lines
