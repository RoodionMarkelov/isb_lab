import os

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricKey:
    """
    class for SymmetricKey
    @methods:
        serialize_key: Сериализует симметричный ключ в файл.
        deserialize_key: Десериализует симметричный ключ из файла.
        generate_key: Генерирует симметричный ключ.
        encrypt_symmetric: Шифрует текст симметричным ключом.
        decrypt_symmetric: Дешифрует текст симметричным ключом ключом.
    """

    def serialize_key(self, path_to_symmetric_key: str, symmetric_key: bytes) -> None:
        """
        Метод сериализует симметричный ключ(symmetric_key) в файл path_to_symmetric_key.
        @param path_to_symmetric_key: путь до файла для симмитричного ключа. Тип str.
        @param symmetric_key: симметричный ключ. Тип bytes.
        """
        try:
            with open(path_to_symmetric_key, 'wb') as file:
                file.write(symmetric_key)
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def deserialize_key(self, path_to_symmetric_key: str) -> bytes:
        """
        Метод десериализует симметричный ключ из файла path_to_symmetric_key.
        @param path_to_symmetric_key: путь до файла с симметричным ключом. Тип str.
        @return symmetric_key: симметричный ключ. Тип bytes.
        """
        try:
            with open(path_to_symmetric_key, mode='rb') as key_file:
                symmetric_key = key_file.read()
            return symmetric_key
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def generate_key(self, number_of_bites: int) -> bytes:
        """
        Метод генерирует симметричный ключ с заданным количеством битов number_of_bites.
        @param number_of_bites: количество битов для симмитричного ключаю Тип int.
        @return symmetric_key: симметричный ключ. Тип bytes.
        """
        try:
            symmetric_key = bytes(os.urandom(number_of_bites))
            return symmetric_key
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        raise

    def encrypt_symmetric(self, text: str, symmetric_key: bytes, number_of_bites: int) -> bytes:
        """
        Метод шифрует текст(text) с помощью симметричного ключа(symmetric_key) с заданным
        количеством битов(number_of_bites). Возвращает зашифрованный текст.
        @param text: текст для шифрования. Тип str.
        @param symmetric_key: симмитричный ключ для шифрования. Тип bytes.
        @param number_of_bites: количество битов для шифрования. тип int.
        @return encrypted_text: зашифрованный текст.
        """
        try:
            padder = padding.ANSIX923(number_of_bites).padder()
            padded_text = padder.update(text) + padder.finalize()
            iv = os.urandom(number_of_bites)
            cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
            encryptor = cipher.encryptor()
            encrypted_text = encryptor.update(padded_text) + encryptor.finalize()
            return encrypted_text
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def decrypt_symmetric(self, encrypted_text: bytes, symmetric_key: bytes, number_of_bites: int) -> str:
        """
        Метод дешифрует зашифрованный текст(encrypted_text) с помощью симметричного ключа(symmetric_key)
        с заданным количеством битов(number_of_bites).
        @param encrypted_text: зашифрованный текст. Тип bytes.
        @param symmetric_key: симмитричный ключ для дешифрования. Тип bytes.
        @param number_of_bites: количество битов для дешифрования. Тип int.
        @return unpadded_decrypted_text.decode('UTF-8'): расшифрованный текст. Тип str.
        """
        try:
            iv = os.urandom(number_of_bites)
            cipher = Cipher(algorithms.AES(symmetric_key), modes.CBC(iv))
            decryptor = cipher.decryptor()
            decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
            unpadder = padding.ANSIX923(number_of_bites).unpadder()
            unpadded_decrypted_text = unpadder.update(decrypted_text) + unpadder.finalize()
            return unpadded_decrypted_text.decode('UTF-8')
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise
