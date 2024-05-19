def save_text(file_name: str, text: bytes):
    """
    Функция записывает текст (text) в файл с названием file_name.
    @param file_name: название файла для записи текста. Тип str.
    @param text: текст для сохранения  в байтах. Тип bytes.
    """
    try:
        with open(file_name, 'wb') as file:
            file.write(text)
    except FileNotFoundError:
        print("Файл не найден.")
        raise
    except Exception as e:
        print(f"Произошла ошибка save_text: {e}")
        raise


def save_text_str(file_name: str, text: str):
    """
    Функция записывает текст (text) в файл с названием file_name.
    @param file_name: название файла для записи текста. Тип str.
    @param text: текст для сохранения  в.виде строки Тип str.
    """
    try:
        with open(file_name, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print("Файл не найден.")
        raise
    except Exception as e:
        print(f"Произошла ошибка save_text_str: {e}")
        raise


def read_text(file_name: str):
    """
    Функция считывает текст из файла с названием file_name. Затем возвращает считанный текст.
    @param file_name: название файла для считывания.Тип str.
    @return content: содержимое файла. Тип str.
    """
    try:
        with open(file_name, mode='rb') as key_file:
            content = key_file.read()
        return content
    except FileNotFoundError:
        print("Файл не найден.")
        raise
    except Exception as e:
        print(f"Произошла ошибка read_text: {e}")
        raise
