import random
import requests
from string import ascii_letters, digits, punctuation
from config import API, DOMAINES

#TO be refactored

chars = ascii_letters + digits + punctuation
    
    
def create_email(login: str = None, domain: str = None) -> str:
    """ Create a new email account """
    if not login:
        login = generate_login()
    if not domain:
        domain = pick_domain()
    mail = u'{0}@{1}'.format(login, domain)
    # TODO: Create validation tests
    requests.get("{API}?login={login}&domain={domain}")
    return mail

def check_mail(mail: str) -> None:
    # TODO: Create validation tests
    login, domain = mail.split()
    pass

def generate_login(length: int = 6) -> str:
    return ''.join(random.choice(ascii_letters) for _ in range(length))

def pick_domain() -> str:
    return random.choice(DOMAINES)
