import random
import requests
from string import ascii_letters
from config import API, DOMAINES
from validation import assert_mail, assert_str, assert_login
    
def create_email(login: str = None, domain: str = None) -> str:
    """ Create a new email account """
    if not login:
        login = generate_login()
    if not domain:
        domain = pick_domain()
    
    assert_login(login)
    assert_str(domain, has_int = True, has_special_char = True)
    mail = u'{0}@{1}'.format(login, domain)
    assert_mail(mail)
    
    requests.get(f"{API}?login={login}&domain={domain}")
    return mail

def check_mail(mail: str) -> None:
    assert_mail(mail)
    login, domain = mail.split('@')
    assert_login(login)
    assert_str(domain, has_int = True, has_special_char = True)

def generate_login(length: int = 6) -> str:
    return ''.join(random.choice(ascii_letters) for _ in range(length))

def pick_domain() -> str:
    return random.choice(DOMAINES)
