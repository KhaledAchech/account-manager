import random
import secrets
from string import ascii_letters, digits, punctuation

class Email:
    
    suffix_cntr: int = 0
    chars = ascii_letters + digits + punctuation
    
    def __init__(self) -> None:
        self.suffix = '-test-'.join(self.suffix_cntr)
    
    def create_email(self, login: str = 'john.doe', domaine: str = '@gmail.com') -> str:
        """ Create a new email account """
        if not login:
            login = self.generate_login()
        self.mail = u'{0}{1}{2}'.format(login, self.suffix, domaine)
        # TODO: Create validation tests
        password = self.generate_password()
        return self.mail

    def generate_login(self, length: int = 6) -> str:
        return ''.join(random.choice(ascii_letters) for i in range(length))

    def generate_password(self, length: int = 8) -> str:
        return ''.join(secrets.choice(self.chars) for i in range(length))
