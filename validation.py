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

def assert_data(data: object = None) -> bool:
    assert data is not None, ERROR + 'Unindefined object! {data}'
    assert isinstance(data, (dict, list, set)), ERROR + 'Unothorized data type! {data}'
    if len(data) == 0:
        print(WARNING + f'This object is empty, object: {data}.')
        return False
    
    try:
        for part in data:
            if isinstance(part, str):
                assert_str(part)
            if isinstance(part, int):
                assert_int(part)
            if isinstance(part, dict):
                assert_dict(part)
    except TypeError: 
        print(WARNING + f'{part} is not iterable')
        return False
    
    return True

def assert_dict(dictionary: dict = None) -> bool:
    assert isinstance(dictionary, dict), ERROR + 'Invalid data type, it should be a dictionary!'
    if len(dictionary) == 0:
        print(WARNING + f'This dictionary is empty: {dictionary}.')
        return False
    return True

def assert_int(integer: int = None) -> None:
    assert isinstance(integer, int), ERROR + 'Invalid data type, it should be an integer!'

def assert_str(string: str = None, has_int: bool = False, has_special_char: bool = False) -> bool:
    assert isinstance(string, str), ERROR + 'Invalid data type it should be a string!'
    
    if not (STR_REGEX.match(string)):
        print(WARNING + f'Invalid string: {string}.')
        return False
    if has_int and not(INT_REGEX.match(string)):
        print(INFO + 'This input needs to have digits.')
        return False
    if has_special_char and not(SPECIAL_CHARS_REGEX.match(string)):
        print(INFO + 'This input needs to have special characters.')
        return False
    
    return True

def assert_password(password: str = None, min_length: str = 8) -> bool:
    assert_str(password, has_int = True, has_special_char = True)
    
    if len(password) < min_length: 
        print(INFO + f'Password should be at least {min_length} chars long.')
        return False
    if not(PASSWORD_REGEX.match(password)):
        print(INFO + 'Password should have at least one uppercase character, one lowercase character, one digit and one special character.')
        return False

    return True

def assert_menu_action(action: dict = None) -> None:
    assert_int(action)
    assert action in ACTIONS,  ERROR + 'Action N°={action} is uninedfined.'

init(autoreset=True)
