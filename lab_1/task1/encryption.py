import os

import key_for_task1 as key


def encryption(message: str) -> str:
    """
    Функция шифрует переданное сообщение согласно "квадрату Полибия".
    :param message:
    :return str:
    """
    message = message.lower()
    result = ""
    for letter in message:
        if (letter in key.signs):
            result += letter
        else:
            place_of_letter = key.get_i_j(letter)
            result += str(place_of_letter)
    return result


def encryption_text(path: str) -> None:
    """
    Функция считывает сообщение из переданного файла, шифрует его и записывает в новый файл.
    :param path:
    :return None:
    """
    os.walk("texts")
    with open(path, "r", encoding="UTF-8") as file1:
        text = " ".join(line.rstrip() for line in file1)
    encryption_text_str = encryption(text)
    with open('texts/task1_encryption_text.txt', 'w', encoding='utf-8') as file2:
        file2.write(encryption_text_str)


if __name__ == "__main__":
    encryption_text("texts/task1_text_for_encryption.txt")
