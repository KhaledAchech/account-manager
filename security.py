import bcrypt
import base64
import json

from cryptography.fernet import Fernet
from config import fetch_master_password, write_config, read_fernet_key


class SecurityAgent(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SecurityAgent, cls).__new__(cls)
            cls.instance._init_instance()
        return cls.instance

    def _init_instance(self):
        # Check if a key is already stored, otherwise generate and store a new one
        fernet_key = read_fernet_key()
        if fernet_key is None:
            fernet_key = Fernet.generate_key()
            write_config("Security", "fernet_key",
                         self.encode_base64(fernet_key))

        self.encryption_key = self.decode_base64(fernet_key)
        self.cipher = Fernet(self.encryption_key)

    def encode_base64(self, data):
        return base64.b64encode(data).decode("utf-8")

    def decode_base64(self, data):
        return base64.b64decode(data)

    def check_master_password(self) -> bool:
        ''' check the existance of the master password; it will return True if it exists otherwise False. '''
        return not (not fetch_master_password())

    def set_master_password(self, password: str) -> None:
        password = self.encrypt_password(password)
        write_config("Other", "master_password",
                     base64.b64encode(password).decode('utf-8'))

    def get_master_password(self) -> None:
        if not self.check_master_password():
            return self.set_master_password()
        return fetch_master_password()

    def encrypt_password(self, password: str) -> bytes:
        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt(rounds=15)
        return bcrypt.hashpw(bytes, salt)

    def verify_master_password(self, given_password: str) -> bool:
        return bcrypt.checkpw(given_password.encode("utf-8"), fetch_master_password())

    def encrypt_credentials(self, credentials: dict) -> bytes:
        credentials_bytes = json.dumps(credentials).encode("utf-8")
        encrypted_credentials = self.cipher.encrypt(credentials_bytes)
        # Encode the encrypted credentials to Base64 before storing
        return base64.b64encode(encrypted_credentials)

    def decrypt_credentials(self, credentials: bytes) -> dict:
        # Decode from Base64 before decrypting
        encrypted_credentials = base64.b64decode(credentials)
        decrypted_credentials_bytes = self.cipher.decrypt(
            encrypted_credentials)
        decrypted_credentials = json.loads(
            decrypted_credentials_bytes.decode("utf-8"))
        return decrypted_credentials


agent = SecurityAgent()
