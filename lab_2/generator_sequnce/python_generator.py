import random


def random_sequence():
    result = ""
    for i in range(0, 128):
        result = result + str(random.randint(0, 1))
    return result


def main():
    string = random_sequence()
    print(string)


if __name__ == "__main__":
    main()
