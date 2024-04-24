import random
import sys


def random_sequence() -> str:
    """
    Функция генерирует два рандомных целых числа переводит их в битовый формат
    и записывает результаты перевода в строку result. После строка возращается.
    :return result(str):
    """
    try:
        result = ""
        for i in range(0, 2):
            number = random.randint(0, sys.maxsize)
            str_tmp = '{:b}'.format(number)
            if len(str_tmp) < 64:
                for j in range(0, 64 - len(str_tmp)):
                    str_tmp = '0' + str_tmp
            result = str_tmp + result
        return result
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise


def main() -> None:
    """
    Функция генерирует случайную последовательность и выводит её.
    :return None:
    """
    try:
        string = random_sequence()
        print(string)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise


if __name__ == "__main__":
    main()
