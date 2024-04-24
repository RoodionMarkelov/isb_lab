import json
import math
import os

from mpmath import gammainc
from scipy.special import erfc
from constants import PATH, LENGTH_OF_BLOCK, PI_I


def read_json_file(file_path: str) -> dict:
    """
    Функция считывает данные из JSON файла.
    :param file_path: указывает на расположение JSON файла.
    :return dict:
    """
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            json_data = json.load(file)
            return json_data
    except FileNotFoundError:
        print("Файл не найден.")
    except json.JSONDecodeError:
        print("Ошибка при считывании JSON-данных.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def frequency_bitwise_test(sequence: str) -> float:
    """
    Функция принимает последовательность бит в виде строки,
    а затем рассчитывает P-значение для частотного побитового теста
    и возвращает его.
    :param sequence: последовательность бит в виде строки(str).
    :return float:
    """
    try:
        N = len(sequence)
        sum = 0
        for bit in sequence:
            if bit == "0":
                sum -= 1
            else:
                sum += 1
        S_N = (1.0 / math.sqrt(N)) * sum
        P_value = erfc(S_N / math.sqrt(2))
        if P_value < 0 or P_value > 1:
            raise ValueError('P should be in range [0, 1]')
        return P_value
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return P_value


def similar_sequences_test(sequence: str) -> float:
    """
    Функция принимает последовательность бит в виде строки,
    а затем рассчитывает P-значение для теста на одинаковые подряд идущие биты
    и возвращает его.
    :param sequence: последовательность бит в виде строки(str).
    :return float:
    """
    try:
        N = len(sequence)
        sum = 0
        for bit in sequence:
            if bit == "1":
                sum += 1
        proportion_of_ones = sum / N
        if abs(proportion_of_ones - (1 / 2)) < 2 / math.sqrt(N):
            V_n = 0
            for i in range(0, N - 1):
                if (sequence[i] != sequence[i + 1]):
                    V_n += 1
            P_value = erfc(
                abs(V_n - 2 * N * proportion_of_ones * (1 - proportion_of_ones)) / (
                        2 * math.sqrt(2 * N) * proportion_of_ones * (
                        1 - proportion_of_ones)))
            if P_value < 0 or P_value > 1:
                raise ValueError('P should be in range [0, 1]')
            return P_value
        else:
            return 0
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def longest_ones_sequence_test(sequence: str):
    """
    Функция принимает последовательность бит в виде строки,
    а затем рассчитывает P-значение для теста на самую длинную
    последовательность единиц в блоке и возвращает его.
    :param sequence:  последовательность бит в виде строки(str).
    :return float:
    """
    try:
        blocks = []
        for i in range(0, int(len(sequence) / LENGTH_OF_BLOCK)):
            blocks.append(sequence[i * LENGTH_OF_BLOCK: (i + 1) * LENGTH_OF_BLOCK])
        V = [0, 0, 0, 0]
        for block in blocks:
            count = 0
            max_length = 0
            for bit in block:
                if bit == "1":
                    count += 1
                    max_length = max(max_length, count)
                else:
                    count = 0
            if max_length <= 1:
                V[0] += 1
            if max_length == 2:
                V[1] += 1
            if max_length == 3:
                V[2] += 1
            if max_length >= 4:
                V[3] += 1
        Xi_in_2 = 0
        for i in range(0, 4):
            Xi_in_2 += pow((V[i] - 16 * PI_I[i]), 2) / (16 * PI_I[i])
        P_value = gammainc(1.5, (Xi_in_2 / 2))
        if P_value < 0 or P_value > 1:
            raise ValueError('P should be in range [0, 1]')
        return P_value
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main() -> None:
    """
    Функция считывает из Json файла последовальности бит,
    полученные из генераторов рандомных чисел C++, JAVA, Python.
    Затем проводит тесты для каждого из них.
    :param :
    :return None:
    """
    try:
        absolute_path = os.path.abspath(os.getcwd())
        json_data = read_json_file(absolute_path + PATH)
        if json_data:
            CPP_SEQUENCE = json_data.get("CPP", "")
            JAVA_SEQUENCE = json_data.get("JAVA", "")
            PYTHON_SEQUENCE = json_data.get("PYTHON", "")
        if CPP_SEQUENCE and JAVA_SEQUENCE and PYTHON_SEQUENCE:
            print("Tests for CPP_SEQUENCE:")
            print("Frequency bitwise test: P = " + str(frequency_bitwise_test(CPP_SEQUENCE)))
            print("Similar sequences test: P = " + str(similar_sequences_test(CPP_SEQUENCE)))
            print("Longest ones sequence test: P = " + str(longest_ones_sequence_test(CPP_SEQUENCE)))
            print("Tests for JAVA_SEQUENCE:")
            print("Frequency bitwise test: P = " + str(frequency_bitwise_test(JAVA_SEQUENCE)))
            print("Similar sequences test: P = " + str(similar_sequences_test(JAVA_SEQUENCE)))
            print("Longest ones sequence test: P = " + str(longest_ones_sequence_test(JAVA_SEQUENCE)))
            print("Tests for PYTHON_SEQUENCE:")
            print("Frequency bitwise test: P = " + str(frequency_bitwise_test(PYTHON_SEQUENCE)))
            print("Similar sequences test: P = " + str(similar_sequences_test(PYTHON_SEQUENCE)))
            print("Longest ones sequence test: P = " + str(longest_ones_sequence_test(PYTHON_SEQUENCE)))
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
