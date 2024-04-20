import os
import logging
import key_for_task1 as key

from lab_1 import read_json
from constants import path, signs


def get_i_j(letter: str) -> tuple:
    """
    Функция возращает индекс строки и столбца letter - буквы из матрицы букв.
    Возвращает неизменяемый список(tuple) вида (i, j), где i - индекс строки, а j - индекс столбца.
    :param letter:
    :return tuple:
    """
    try:
        for i in range(0, len(key.matrix_of_letter)):
            try:
                j = key.matrix_of_letter[i].index(letter)
            except Exception:
                continue
            if (letter == key.matrix_of_letter[i][j]):
                return i, j
    except Exception as e:
        logging.error(f"Ошибка в функции get_i_j(letter): {e}")
        raise


def encryption(message: str) -> str:
    """
    Функция шифрует переданное сообщение(message) согласно "квадрату Полибия".
    Возвращает результат в виде строки(str).
    :param message:
    :return str:
    """
    message = message.lower()
    result = ""
    try:
        for letter in message:
            if (letter in signs):
                result += letter
            else:
                place_of_letter = get_i_j(letter)
                if place_of_letter != None:
                    result += str(place_of_letter)
        return result
    except Exception as e:
        logging.error(f"Ошибка в функции encryption(message): {e}")


def message_encryption(file_name: str) -> str:
    """
    Функция  считывает сообщение из файла с именем file_name, затем шифрует его
    и возращает результат в виде строки(str).
    :param file_name:
    :return str:
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            message = file.read()
            encrypted_text = encryption(message)
            return encrypted_text
    except FileNotFoundError:
        print("Файл не найден.")


def save_message(file_name: str, message) -> None:
    """
    Функция сохраняет сообщение(message) в указанный файл с именем file_name с перезаписыванием содержимого.
    Создает файл с именем file_name, если такого нет.
    Функция ничего не возвращает.
    :param file_name:
    :param message:
    :return None:
    """
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(message)
    except Exception as e:
        logging.error(f"Ошибка в функции get_i_j(letter): {e}")
        raise


def main() -> None:
    """
    Функция считывает сообщение из файла, шифрует его и записывает в новый файл, заданным пользователем.
    Функция ничего не возвращает.
    :param :
    :return None:
    """
    absolute_path = os.path.abspath(os.getcwd())
    json_data = read_json.read_json_file(absolute_path + path)
    if json_data:
        folder = json_data.get("folder", "")
        path_from = json_data.get("path_from", "")
        path_to = json_data.get("path_to", "")
    if folder and path_from and path_to:
        try:
            encrypted_text = message_encryption(absolute_path + folder + path_from)
            save_message(absolute_path + folder + path_to, encrypted_text)
            print("Текст успешно зашифрован и сохранен в файле.")
        except Exception as e:
            print(f"Произошла ошибка в функции send_encryption_text: {e}")


if __name__ == "__main__":
    main()