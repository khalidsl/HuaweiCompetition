from cryptography.fernet import Fernet

class EncryptionService:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        if isinstance(data, str):
            data = data.encode()
        return self.cipher.encrypt(data)

    def decrypt(self, token):
        decrypted_data = self.cipher.decrypt(token)
        return decrypted_data.decode()