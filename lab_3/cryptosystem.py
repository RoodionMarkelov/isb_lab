import symmetric_key
import asymmetric_key

from save_and_read_text import read_text, save_text


class Cryptosystem:
    def __init__(self, number_of_bites):
        self.symmetric = symmetric_key.SymmetricKey()
        self.asymmetric = asymmetric_key.AsymmetricKey()
        self.number_of_bites = number_of_bites

    def generate_keys(self, path_to_symmetric_key, path_to_public_key, path_to_private_key):
        self.symmetric.generate_key(self.number_of_bites)
        keys = self.asymmetric.generate_keys()
        self.asymmetric.serialization_keys(path_to_private_key, path_to_public_key, keys[0], keys[1])
        symmetric_key_encrypted = self.asymmetric.encrypt_text(self.symmetric.symmetric_key, keys[1])
        self.symmetric.serialization_key(path_to_symmetric_key, symmetric_key_encrypted)

    def encrypt(self, path_to_text_for_encryption, path_to_symmetric_key, path_to_private_key,
                path_to_save_encrypted_text):
        encrypted_symmetric_key = self.symmetric.deserialization_key(path_to_symmetric_key)
        decrypted_symmetric_key = self.asymmetric.decrypt_text(path_to_private_key, encrypted_symmetric_key)
        text = read_text(path_to_text_for_encryption)
        encrypted_text = self.symmetric.encrypt_symmetric(text, decrypted_symmetric_key, self.number_of_bites)
        save_text(path_to_save_encrypted_text, encrypted_text)

    def decrypt(self, path_to_encrypted_text, path_to_symmetric_key, path_to_private_key,
                path_to_save_decrypted_text):
        encrypted_symmetric_key = self.symmetric.deserialization_key(path_to_symmetric_key)
        decrypted_symmetric_key = self.asymmetric.decrypt_text(path_to_private_key, encrypted_symmetric_key)
        encrypted_text = read_text(path_to_encrypted_text)
        decrypted_text = self.symmetric.decrypt_symmetric(encrypted_text, decrypted_symmetric_key)
        save_text(path_to_save_decrypted_text, decrypted_text)
