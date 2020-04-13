import logging
from base64 import b64decode, b64encode

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad


class BluePrismAes:
    logger = logging.getLogger(__name__)

    def __init__(self, credentials_key):
        self.private_key = b64decode(credentials_key)

    def decrypt(self, encrypted_string: str) -> str:
        self.logger.info('Decrypting queue item data [%s]', encrypted_string)
        encrypted_tab = encrypted_string.split(':')
        iv = b64decode(encrypted_tab[0])
        encrypted_data = b64decode(encrypted_tab[1])
        cipher = AES.new(self.private_key, AES.MODE_CBC, iv)
        return cipher.decrypt(encrypted_data).decode('utf-8').strip()

    def encrypt(self, string_to_encrypt: str) -> str:
        self.logger.info('Encrypting queue item data [%s]', string_to_encrypt)
        cipher = AES.new(self.private_key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(string_to_encrypt.encode(), AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        return f'{iv}:{ct}'
