import os

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricKey:
    def __init__(self, number_of_bites):
        self.number_of_bites = number_of_bites
        self.symmetric_key = None

    def deserialization_key(self, path_to_symmetric_key):
        with open(path_to_symmetric_key, mode='rb') as key_file:
            content = key_file.read()
        return content

    def serialization_key(self, path_to_symmetric_key):
        with open(path_to_symmetric_key, 'wb') as file:
            file.write(self.symmetric_key)

    def generate_key(self):
        self.symmetric_key = bytes(os.urandom(self.number_of_bites))

    def encrypt_symmetric(self, text, symmetric_key):
        padder = padding.ANSIX923(self.number_of_bites).padder()
        padded_text = padder.update(text) + padder.finalize()
        iv = os.urandom(self.number_of_bites)
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
        return encrypted_text

    def decrypt_symmetric(self, encrypted_text, symmetric_key):
        iv = os.urandom(
            self.number_of_bites)
        cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
        unpadder = padding.ANSIX923(self.number_of_bites).unpadder()
        unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
        return unpadded_decrypted_text.decode('UTF-8')
