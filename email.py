import random
import secrets
from string import ascii_letters, digits, punctuation

#TO be refactored

chars = ascii_letters + digits + punctuation
    
    
def create_temp_email(login: str = 'john.doe', domaine: str = '@gmail.com') -> str:
    """ Create a new email account """
    # TODO: use this for reference
    if not login:
        login = generate_login()
    mail = u'{0}{1}'.format(login, domaine)
    # TODO: Create validation tests
    return mail

def generate_login(length: int = 6) -> str:
    return ''.join(random.choice(ascii_letters) for i in range(length))

def generate_password(length: int = 8) -> str:
    return ''.join(secrets.choice(chars) for i in range(length))
