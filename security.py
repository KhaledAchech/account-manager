import bcrypt

from config import fetch_master_password, write_config
from validation import assert_password

class SecurityAgent(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SecurityAgent, cls).__new__(cls)
        return cls.instance
    
    def check_master_password(self) -> bool:
        ''' check the existance of the master password; it will return True if it exists otherwise False. '''
        return not(not fetch_master_password())

    def set_master_password(self, password: str) -> None:
        if not assert_password(password): return
        password = self.encrypt_password(password)
        write_config("Other", password)

    def get_master_password(self) -> None:
        if not self.check_master_password():
            return self.set_master_password()
        return fetch_master_password()

    def encrypt_password(self, password: str) -> str:
        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt(rounds=15)
        return bcrypt.hashpw(bytes, salt)
    
    def verify_master_password(self, given_password: str) -> bool:
        if not assert_password(given_password): return False
        return bcrypt.checkpw(given_password, fetch_master_password())

    def check_lockout_state(self) -> None:
        pass

    def change_lockout_state(self) -> None:
        pass

    def get_lockout_timestamp(self) -> None:
        pass

    def set_lockout_timestamp(self) -> None:
        pass

agent = SecurityAgent()
