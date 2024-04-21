import json
import math

from mpmath import gammainc
from scipy.special import erfc
from constants import PATH, LENGTH_OF_BLOCK, PI_I


def read_json_file(file_path: str) -> dict:
    """
    Функция считывает данные из JSON файла.
    :param file_path:
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
    N = len(sequence)
    sum = 0
    for bit in sequence:
        if bit == "0":
            sum -= 1
        else:
            sum += 1
    S_N = (1.0 / math.sqrt(N)) * sum
    P_value = erfc(S_N)
    return P_value


def similar_test(sequence: str) -> float:
    N = len(sequence)
    sum = 0
    for bit in sequence:
        if bit == "1":
            sum += 1
    proportion_of_ones = sum / N
    if abs(proportion_of_ones - (1 / 2)) < 2 / math.sqrt(N):
        return 0
    else:
        V_n = 0
        for i in range(0, N - 1):
            if (sequence[i] != sequence[i + 1]):
                V_n += 1
        P_value = erfc(
            abs(V_n - 2 * N * proportion_of_ones(1 - proportion_of_ones)) / (2 * math.sqrt(2 * N) * proportion_of_ones(
                1 - proportion_of_ones)))
        return P_value


def longest_sequence_test(sequence: str):
    blocks = []
    for i in range(0, int(len(sequence) / LENGTH_OF_BLOCK)):
        blocks.append(sequence[i * LENGTH_OF_BLOCK: (i + 1) * LENGTH_OF_BLOCK])
    V = [0, 0, 0, 0]
    for block in blocks:
        count = 0
        max_length = 0
        for bit in block:
            if bit == 1:
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
    P_value = gammainc(1.5, Xi_in_2 / 2)
    return P_value


def main():
    return


if __name__ == "__main__":
    # main()
    print(longest_sequence_test(
        "11110001001000101111110101010100100000110011010110110111011101110001010111111001011110001101010010111000110001100110001100011111"))
