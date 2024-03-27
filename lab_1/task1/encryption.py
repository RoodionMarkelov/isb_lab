import os
import logging
import constants_sign
import key_for_task1 as key


def get_i_j(letter: str) -> tuple:
    """
    Функция возращает индекс строки и столбца буквы из матрицы укв.
    :param letter:
    :return tuple:
    """
    try:
        for i in range(0, len(key.matrix_of_letter)):
            for j in range(0, len(key.matrix_of_letter[0])):
                if (letter == key.matrix_of_letter[i][j]):
                    return i, j
    except Exception:
        logging.error(f"Ошибка в функции get_i_j(letter): индекс не найден")


def encryption(message: str) -> str:
    """
    Функция шифрует переданное сообщение согласно "квадрату Полибия".
    :param message:
    :return str:
    """
    message = message.lower()
    result = ""
    try:
        for letter in message:
            if (letter in constants_sign.signs):
                result += letter
            else:
                place_of_letter = get_i_j(letter)
                result += str(place_of_letter)
        return result
    except Exception:
        logging.error(f"Ошибка в функции encryption(message): не удалось закодировать сообщение")


def encryption_text() -> None:
    """
    Функция считывает сообщение из переданного пользователем файла, шифрует его и записывает в новый файл, заданным пользователем.
    :param :
    :return None:
    """
    try:
        path_from = input("Введите полный путь к файлу с сообщением:")
        with open(path_from, "r", encoding="UTF-8") as file1:
            text = " ".join(line.rstrip() for line in file1)
        encryption_text_str = encryption(text)
        try:
            path_to = input("Введите полный путь к папке для сохранения сообщения:")
            file_name = input("Введите название для файла:")
            full_path = os.path.join(path_to, file_name)
            with open(full_path, 'w', encoding='utf-8') as file2:
                file2.write(encryption_text_str)
        except FileNotFoundError:
            print('Ошибка файл не найден')
    except FileNotFoundError:
        print('Ошибка файл не найден')


if __name__ == "__main__":
    encryption_text()
