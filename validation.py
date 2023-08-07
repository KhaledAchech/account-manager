import re
from config import VALIDATION

INFO = VALIDATION.get("info")
WARNING = VALIDATION.get("warning")
ERROR = VALIDATION.get("ERROR")

STR_REGEX = re.compile('^[A-Za-z]+$')
INT_REGEX = re.compile('\d+')
SPECIAL_CHARS_REGEX = re.compile('[\W_]+')
PASSWORD_REGEX = re.compile('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')

def assert_data(data: object = None) -> None:
    assert data is not None, '\{ERROR} This is an empty object!'
    for part in data:
        if isinstance(part, str):
            assert_str(part)
        if isinstance(part, int):
            assert_int(part)
        if isinstance(part, dict):
            assert_dict(part)

def assert_dict(dictionary: dict = None) -> None:
    assert isinstance(dictionary, dict), '\{ERROR} Invalid data type, it should be a dictionary!'
    assert len(dictionary) > 0, '\{WARNING} This dictionary is empty.'

def assert_int(integer: int = None) -> None:
    assert isinstance(integer, int), '\{ERROR} Invalid data type, it should be an integer!'

def assert_str(string: str = None, has_int: bool = False, has_special_char: bool = False) -> None:
    assert STR_REGEX.match(string), '\{WARNING} This input needs to have alphabets.'
    if has_int:
        assert INT_REGEX.match(string), '\{WARNING} This input needs to have digits.'
    if has_special_char:
        assert SPECIAL_CHARS_REGEX.match(string), '\{WARNING} This input needs to have special characters.'

def assert_passowrd(password: str = None, min_length: str = 8) -> None:
    assert_str(password, True, True)
    assert len(password) >= min_length, '\{INFO} Password should be at least {min_length} chars long.'
    assert PASSWORD_REGEX.match(password), '\{INFO} Password should have at least one uppercase character, one lowercase character, one digit and one special character.'

def assert_temp_email_login(login: str = None) -> None:
    pass

def assert_temp_email_domain(domain: str = None) -> None:
    pass

def assert_menu_action(action: dict = None) -> None:
    pass

