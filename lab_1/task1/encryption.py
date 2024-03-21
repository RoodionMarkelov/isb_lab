import key_for_task1 as key

def encryption(message: str):
    message = message.lower()
    result = ""
    for letter in message:
        if (letter in key.signs):
            result += letter
        else:
            place_of_letter = key.get_i_j(letter)
            result += str(place_of_letter)
    return result

def encryption_text(path: str):
    with open(path, "r", encoding="UTF-8") as file1:
        text = " ".join(line.rstrip() for line in file1)
    encryption_text_str = encryption(text)
    with open('texts/encryption_text.txt', 'w', encoding='utf-8') as file2:
        file2.write(encryption_text_str)

if __name__ == "__main__":
    encryption_text("texts/text_for_encryption.txt")