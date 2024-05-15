def save_text(file_name: str, text: bytes):
    with open(file_name, 'wb') as file:
        file.write(text)


def read_text(file_name: str):
    with open(file_name, mode='rb') as key_file:
        content = key_file.read()
    return content
