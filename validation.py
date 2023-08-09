import re
from colorama import init, Fore, Back

INFO = Back.BLUE + Fore.WHITE
WARNING = Back.YELLOW + Fore.BLACK
ERROR = Back.RED + Fore.BLACK

ACTIONS = [-1, 0, 1]

STR_REGEX = re.compile('^[A-Za-z]+$')
INT_REGEX = re.compile('\d+')
SPECIAL_CHARS_REGEX = re.compile('[\W_]+')
PASSWORD_REGEX = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

def assert_data(data: object = None) -> None:
    assert data is not None, ERROR + 'Unindefined object! {object}'
    if isinstance(data, (dict, list, set)): assert len(data) > 0, WARNING + 'This object is empty, {object}.'
    for part in data:
        if isinstance(part, str):
            assert_str(part)
        if isinstance(part, int):
            assert_int(part)
        if isinstance(part, dict):
            assert_dict(part)

def assert_dict(dictionary: dict = None) -> None:
    assert isinstance(dictionary, dict), ERROR + 'Invalid data type, it should be a dictionary!'
    assert len(dictionary) > 0, WARNING + 'This dictionary is empty.'

def assert_int(integer: int = None) -> None:
    assert isinstance(integer, int), ERROR + 'Invalid data type, it should be an integer!'

def assert_str(string: str = None, has_int: bool = False, has_special_char: bool = False) -> None:
    assert STR_REGEX.match(string), ERROR + 'Invalid string: {string}.'
    if has_int:
        assert INT_REGEX.match(string), INFO + 'This input needs to have digits.'
    if has_special_char:
        assert SPECIAL_CHARS_REGEX.match(string), INFO + 'This input needs to have special characters.'

def assert_password(password: str = None, min_length: str = 8) -> None:
    assert_str(password, True, True)
    assert len(password) >= min_length, INFO + 'Password should be at least {min_length} chars long.'
    assert PASSWORD_REGEX.match(password), INFO + 'Password should have at least one uppercase character, one lowercase character, one digit and one special character.'

def assert_menu_action(action: dict = None) -> None:
    assert_int(action)
    assert action in ACTIONS,  WARNING + 'Action N°={action} is uninedfined.'

init(autoreset=True)
assert_data(None)