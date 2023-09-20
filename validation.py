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
MAIL_REGEX = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

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

def assert_bool(condition: bool, expected_result: bool, info_message: str) -> bool:
    assert isinstance(condition, bool), ERROR + 'Invalid data type, it should be a boolean expression!'
    assert isinstance(expected_result, bool), ERROR + 'Invalid data type, it should be a boolean expression!'
    assert isinstance(info_message, str), ERROR + 'Invalid data type it should be a string!'
    if condition != expected_result: INFO + info_message
    return condition == expected_result

def assert_int(integer: int = None) -> None:
    assert isinstance(integer, int), ERROR + 'Invalid data type, it should be an integer!'

def assert_str(string: str = None, has_int: bool = False, has_special_char: bool = False) -> bool:
    assert isinstance(string, str), ERROR + 'Invalid data type it should be a string!'
    
    if not (STR_REGEX.match(string)) and not(has_int) and not(has_special_char):
        print(WARNING + f'Invalid string: {string}.')
        return False
    if has_int and not(INT_REGEX.search(string)):
        print(INFO + f'This input needs to have digits: {string}.')
        return False
    if has_special_char and not(SPECIAL_CHARS_REGEX.search(string)):
        print(INFO + f'This input needs to have special characters: {string}.')
        return False
    
    return True

def assert_mail(mail: str) -> bool:
    assert_str(mail, has_int = True, has_special_char = True)
    if not(MAIL_REGEX.match(mail)): print(WARNING + f'Invalid mail: {mail}.')
    return MAIL_REGEX.match(mail)

def assert_login(login: str) -> bool:
    assert_str(login, has_int = True, has_special_char = True)
    if len(login) < 6: print(WARNING + f'Login should be at least 6 chars long.')
    return len(login) < 6

def assert_password(password: str = None, min_length: str = 8) -> bool:
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

def assert_config(section: str, option: str, value: str) -> None:
    assert assert_str(section) and assert_str(option, has_special_char=True) and assert_str(value, has_int=True), ERROR + 'Invalid configuration! Verify the section: {section}, the option: {option} and the value: {value}.'

init(autoreset=True)
