import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def serialization_private(file_name: str, private_key):
    with open(file_name, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                    encryption_algorithm=serialization.NoEncryption()))


def serialization_public(file_name: str, public_key):
    with open(file_name, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PublicFormat.SubjectPublicKeyInfo))


def read_text(file_name: str):
    with open(file_name, mode='rb') as key_file:
        content = key_file.read()
    return content


def save_text(file_name: str, text: bytes):
    with open(file_name, 'wb') as file:
        file.write(text)


def serialization_symmetric(file_name: str, symmetric_key):
    with open(file_name, 'wb') as key_file:
        key_file.write(symmetric_key)


def deserialization_private(file_name: str):
    with open(file_name, 'rb') as pem_in:
        private_bytes = pem_in.read()
    d_private_key = load_pem_private_key(private_bytes, password=None, )
    return d_private_key


def deserialization_public(file_name: str):
    with open(file_name, 'rb') as pem_in:
        public_bytes = pem_in.read()
    d_public_key = load_pem_public_key(public_bytes)
    return d_public_key


def decrypt_symmetric_key(path_to_private_key: str, path_to_symmetric_key: str):
    encrypted_symmetric_key = read_text(path_to_symmetric_key)
    private_key = deserialization_private(path_to_private_key)
    symmetric_key = private_key.decrypt(encrypted_symmetric_key,
                                        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))
    return symmetric_key


def generate_keys(path_to_symmetric: str, path_to_public_key: str, path_to_private_key: str, number_of_bites: int):
    symmetric_key = bytes(os.urandom(number_of_bites))
    keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    private_key = keys
    public_key = keys.public_key()
    serialization_private(path_to_private_key, private_key)
    serialization_public(path_to_public_key, public_key)
    symmetric_key_to_save = public_key.encrypt(symmetric_key,
                                               padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(),
                                                            label=None))
    serialization_symmetric(path_to_symmetric, symmetric_key_to_save)


def encrypt_data(path_to_text_for_encryption: str, path_to_symmetric_key: str, path_to_private_key: str,
                 path_to_save_encrypted_text: str, number_of_bites: int):
    symmetric_key = decrypt_symmetric_key(path_to_private_key, path_to_symmetric_key)
    padder = padding.ANSIX923(number_of_bites).padder()
    text = read_text(path_to_text_for_encryption)
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(number_of_bites)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
    save_text(path_to_save_encrypted_text, encrypted_text)


def decrypt_data(path_to_encrypted_text: str, path_to_symmetric_key: str, path_to_private_key: str,
                 path_to_save_dencrypted_text: str, number_of_bites: int):
    symmetric_key = decrypt_symmetric_key(path_to_private_key, path_to_symmetric_key)
    iv = os.urandom(
        number_of_bites)
    cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    encrypted_text = read_text(path_to_encrypted_text)
    decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(number_of_bites).unpadder()
    unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
    save_text(path_to_save_dencrypted_text, unpadded_decrypted_text)
