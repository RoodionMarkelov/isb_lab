from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class AsymmetricKey:
    def __init__(self, number_of_bites):
        self.number_of_bites = number_of_bites
        self.public_key = None
        self.private_key = None

    def serialization_private(self, path_to_private_key):
        with open(path_to_private_key, 'wb') as private_out:
            private_out.write(self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                             format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                             encryption_algorithm=serialization.NoEncryption()))

    def serialization_public(self, path_to_public_key):
        with open(path_to_public_key, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                          format=serialization.PublicFormat.SubjectPublicKeyInfo))

    def serialization_keys(self, path_to_private_key, path_to_public_key):
        self.serialization_private(path_to_private_key)
        self.serialization_public(path_to_public_key)

    def deserialization_private(self, path_to_private_key):
        with open(path_to_private_key, 'rb') as pem_in:
            private_bytes = pem_in.read()
        d_private_key = load_pem_private_key(private_bytes, password=None, )
        return d_private_key

    def deserialization_public(self, path_to_public_key):
        with open(path_to_public_key, 'rb') as pem_in:
            public_bytes = pem_in.read()
        d_public_key = load_pem_public_key(public_bytes)
        return d_public_key

    def generate_keys(self):
        keys = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.private_key = keys
        self.public_key = keys.public_key()

    def encrypt_text(self, text):
        encrypted_text = self.public_key.encrypt(text,
                                                 padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                              algorithm=hashes.SHA256(),
                                                              label=None))
        return encrypted_text

    def decrypt_text(self, encrypted_text):
        decrypted_text = self.private_key.decrypt(encrypted_text,
                                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                               algorithm=hashes.SHA256(), label=None))
        return decrypted_text
