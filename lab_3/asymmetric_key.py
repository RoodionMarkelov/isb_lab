from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class AsymmetricKey:
    """
    class for AsymmetricKey
    @methods:
        serialize_private: Сериализует приватный ключ в файл.
        serialize_public: Сериализует публичный ключ в файл.
        serialize_keys: Сериализует приватный и публичный ключи в файлы.
        deserialize_private: Десериализует приватный ключ из файла.
        deserialize_public: Десериализует публичный ключ из файла.
        generate_keys: Генерирует приватный и публичный ключи.
        encrypt_text: Шифрует текст публичным ключом.
        decrypt_text: Дешифрует текст приватныи ключом.
    """

    def serialize_private(self, path_to_private_key: str, private_key: rsa.RSAPrivateKey) -> None:
        """
        Метод сериализует приватный ключ(private_key) по заданному пути(path_to_private_key).
        @param path_to_private_key: путь до файла для сохранения приватного ключа. Тип str.
        @param private_key: приватный ключ, который нужно сериализовать. Тип rsa.RSAPrivateKey.
        """
        try:
            with open(path_to_private_key, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,

                                                            format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                            encryption_algorithm=serialization.NoEncryption()))
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def serialize_public(self, path_to_public_key: str, public_key: rsa.RSAPublicKey) -> None:
        """
        Метод сериализует публичный ключ(public_key) по заданному пути(path_to_public_key).
        @param path_to_public_key: путь до файла для сохранения публичного ключа. Тип str.
        @param public_key: публичный ключ, который нужно сериализовать. Тип rsa.RSAPublicKey.
        """
        try:
            with open(path_to_public_key, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def serialize_keys(self, path_to_private_key: str, path_to_public_key: str, private_key: rsa.RSAPrivateKey,
                       public_key: rsa.RSAPublicKey) -> None:
        """
        Метод сериализует приватный ключ(private_key) и публичный ключ(public_key) по заданным путям
        (path_to_private_key) и (path_to_public_key).
        @param path_to_private_key: путь до файла для сохранения приватного ключа. Тип str.
        @param path_to_public_key: приватный ключ, который нужно сериализовать. Тип str.
        @param private_key: приватный ключ, который нужно сериализовать. Тип rsa.RSAPrivateKey.
        @param public_key: публичный ключ, который нужно сериализовать. Тип rsa.RSAPublicKey.
        """
        self.serialize_private(path_to_private_key, private_key)

        self.serialize_public(path_to_public_key, public_key)

    def deserialize_private(self, path_to_private_key: str) -> rsa.RSAPrivateKey:
        """
        Метод десиарилизует приватный ключ из указанного файла(path_to_private_key).
        @param path_to_private_key: путь до файла с сохранненым приватным ключом. Тип str.
        @return d_private_key: приватный ключ. Тип rsa.RSAPrivateKey.
        """
        try:
            with open(path_to_private_key, 'rb') as pem_in:
                private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes, password=None, )
            return d_private_key
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def deserialize_public(self, path_to_public_key: str) -> rsa.RSAPublicKey:
        """
        Метод десиарилизует публичный ключ из указанного файла(path_to_public_key).
        @param path_to_public_key: путь до файла с сохранненым публичным ключом. Тип str.
        @return d_public_key: публичный ключ. Тип rsa.RSAPublicKey.
        """
        try:
            with open(path_to_public_key, 'rb') as pem_in:
                public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
            return d_public_key
        except FileNotFoundError:
            print("Файл не найден.")
            raise
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def generate_keys(self) -> tuple:
        """
        Метод генерирует два ключа: приватный(private_key) и публичный(public_key), после чего возвращает их в виде списка.
        @return private_key, public_key:
        """
        try:
            keys = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )
            private_key = keys
            public_key = keys.public_key()
            return private_key, public_key
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def encrypt_text(self, text: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Метод шифрует текст(text) с помощью публичного ключа, после чего возвращает
        зашифрованый текст(encrypted_text).
        @param text: текст, который нужно зашифровать. Тип bytes
        @param public_key: публичный ключ, с помощью которого шифруется текст. Тип rsa.RSAPublicKey
        @return encrypted_text: зашифрованный текст. Тип bytes
        """
        try:
            encrypted_text = public_key.encrypt(text,
                                                padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                             algorithm=hashes.SHA256(),
                                                             label=None))
            return encrypted_text
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise

    def decrypt_text(self, path_to_private_key: str, encrypted_text: bytes) -> bytes:
        """
        Метод дешифрует текст(encrypted_text) с помощью приватного ключа, который
        десиарилизуется из файла(path_to_private_key), после чего возвращает
        разшифрованный текст(decrypted_text).
        @param path_to_private_key: файл с приватным ключом str
        @param encrypted_text: зашифрованный текст. Тип bytes
        @return decrypted_text: разсшифрованный текстю Тип bytes
        """
        try:
            private_key = self.deserialize_private(path_to_private_key)
            decrypted_text = private_key.decrypt(encrypted_text,
                                                 padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                              algorithm=hashes.SHA256(), label=None))
            return decrypted_text
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            raise
