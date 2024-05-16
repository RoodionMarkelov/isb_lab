import json
import sys
import os

from PyQt5.QtWidgets import (
    QMainWindow,
    QToolTip,
    QPushButton,
    QApplication,
    QDesktopWidget,
    QFileDialog,
    QLabel,
    QMessageBox, QComboBox,
)
from PyQt5.QtGui import QIcon, QFont

import cryptosystem
from constants import PATH


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
        raise
    except json.JSONDecodeError:
        print("Ошибка при считывании JSON-данных.")
        raise
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        raise


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.text = None
        self.encrypted_file = None
        self.decrypted_file = None
        self.symmetric_key = None
        self.public_key = None
        self.private_key = None
        self.cryptosystem = None

        QToolTip.setFont(QFont("SansSerif", 14))
        self.setToolTip("Это <b>QWidget</b> виджет")

        self.messagelabel = QLabel(self)
        self.messagelabel.setText("Привет пользователь!")
        self.messagelabel.adjustSize()
        self.messagelabel.move(200, 50)

        self.label_number_of_bits = QLabel(self)
        self.label_number_of_bits.setText("Количество битов:")
        self.label_number_of_bits.adjustSize()
        self.label_number_of_bits.move(290, 207)

        self.UiComponents()

        btn1 = QPushButton("Инициализация криптосистемы по умолчанию", self)
        btn1.setToolTip(
            "Нажмите на кнопку для создание файлов для ключей криптосистемы по умолчанию."
        )
        btn1.clicked.connect(self.create_by_default)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 100)

        btn2 = QPushButton("Инициализация криптосистемы пользователем", self)
        btn2.setToolTip(
            "Нажмите на кнопку для выбора файлов для ключей криптосистемы."
        )
        btn2.clicked.connect(self.create_by_user)
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 150)

        btn3 = QPushButton("Создание ключей", self)
        btn3.setToolTip(
            "Нажмите на кнопку для создание ключей криптосистемы."
        )
        btn3.clicked.connect(self.generate_keys_for_cryptosystem)
        btn3.resize(btn3.sizeHint())
        btn3.move(50, 200)

        btn4 = QPushButton("Зашифровать текст", self)
        btn4.setToolTip(
            "Нажмите на кнопку для шифрования текста."
        )
        btn4.clicked.connect(self.encrypt_text)
        btn4.resize(btn4.sizeHint())
        btn4.move(50, 250)

        btn5 = QPushButton("Дешифровать текст", self)
        btn5.setToolTip(
            "Нажмите на кнопку для дешифрования текста."
        )
        btn5.clicked.connect(self.decrypt_text)
        btn5.resize(btn4.sizeHint())
        btn5.move(50, 300)

        qbtn = QPushButton("Выход", self)
        qbtn.setToolTip("Нажмите для кнопки для выхода.")
        qbtn.clicked.connect(self._quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(350, 400)
        self.resize(500, 500)
        self.center()
        self.setWindowTitle("app")
        self.setWindowIcon(QIcon("web.png"))

        self.show()

    def center(self):
        """Move the window to the center. Return None"""
        location = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        location.moveCenter(center)
        self.move(location.topLeft())

    def get_file(self):
        """Get file from directory"""
        folderpath = QFileDialog.getExistingDirectory(self, "Выберете папку")
        file_name = QFileDialog.getOpenFileName(
            self, "Выберете файл", folderpath
        )
        return file_name[0]

    def create_by_default(self):
        absolute_path = os.path.abspath(os.getcwd())
        json_data = read_json_file(absolute_path + PATH)
        if json_data:
            text = json_data.get("text", "")
            encrypted_file = json_data.get("encrypted_file", "")
            decrypted_file = json_data.get("decrypted_file", "")
            symmetric_key = json_data.get("symmetric_key", "")
            public_key = json_data.get("public_key", "")
            private_key = json_data.get("private_key", "")
        if text and encrypted_file and decrypted_file and symmetric_key and private_key and public_key :
            self.text = absolute_path + text
            self.encrypted_file = absolute_path + encrypted_file
            self.decrypted_file = absolute_path + decrypted_file
            self.symmetric_key = absolute_path + symmetric_key
            self.public_key = absolute_path + public_key
            self.private_key = absolute_path + private_key
            number_of_bites = int(self.find())
            self.cryptosystem = cryptosystem.Cryptosystem(number_of_bites)

    def UiComponents(self):
        self.combo_box = QComboBox(self)

        self.combo_box.setGeometry(400, 200, 50, 30)

        list_of_number_of_bits = ["64", "128", "192"]

        self.combo_box.addItems(list_of_number_of_bits)

    def find(self):

        content = self.combo_box.currentText()

        self.label.setText("Content : " + content)

    def create_by_user(self):
        self.text = self.get_file()
        self.encrypted_file = self.get_file()
        self.decrypted_file = self.get_file()
        self.symmetric_key = self.get_file()
        self.public_key = self.get_file()
        self.private_key = self.get_file()
        number_of_bites = int(self.find())
        self.cryptosystem = cryptosystem.Cryptosystem(number_of_bites)

    def generate_keys_for_cryptosystem(self):
        self.cryptosystem.generate_keys(self.symmetric_key, self.public_key, self.private_key)
        self.messagelabel.setText("Ключи созданы.")

    def encrypt_text(self):
        self.cryptosystem.encrypt(self.text, self.symmetric_key, self.private_key, self.encrypted_file)
        self.messagelabel.setText("Текст зашифрован.")

    def decrypt_text(self):
        self.cryptosystem.decrypt(self.encrypted_file, self.symmetric_key, self.private_key, self.decrypted_file)
        self.messagelabel.setText("Текст дешифрован.")

    def _quit(self):
        """Get MessageBox for exit"""
        reply = QMessageBox.question(
            self,
            "Сообщение",
            "Вы уверены, что хотите выйти?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            QApplication.instance().quit()
        else:
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
