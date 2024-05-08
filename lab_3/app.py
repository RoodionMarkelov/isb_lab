import json
import sys
import os

from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QToolTip,
    QPushButton,
    QApplication,
    QDesktopWidget,
    QFileDialog,
    QLabel,
    QMessageBox,
    QCalendarWidget,
)
from PyQt5.QtGui import QIcon, QFont

from lab_3 import task
from constants import PATH


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        QToolTip.setFont(QFont("SansSerif", 14))

        self.setToolTip("Это <b>QWidget</b> виджет")
        self.label = QLabel(self)
        self.label.setText("Привет пользователь!")
        self.label.adjustSize()
        self.label.move(200, 50)

        self.date = QLabel(self)
        self.temp_morning = QLabel(self)
        self.pres_morning = QLabel(self)
        self.wind_morning = QLabel(self)
        self.temp_evening = QLabel(self)
        self.pres_evening = QLabel(self)
        self.wind_evening = QLabel(self)

        btn1 = QPushButton("Сгенерировать ключи", self)
        btn1.setToolTip(
            "Нажмите на кнопку для генерации симмитричного, открытого и закрытого ключа."
        )
        btn1.clicked.connect(self._generate_keys)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)

        btn2 = QPushButton("Зашифровать данные", self)
        btn2.setToolTip(
            "Нажмите на кнопку для шифрования данных."
        )
        btn2.clicked.connect(self._encrypt)
        btn2.resize(btn2.sizeHint())
        btn2.move(50, 100)

        btn3 = QPushButton("Дешифровать данные", self)
        btn3.setToolTip(
            "Нажмите на кнопку для дешифрования данных."
        )
        btn3.clicked.connect(self._decrypt)
        btn3.resize(btn3.sizeHint())
        btn3.move(50, 150)

        qbtn = QPushButton("Выход", self)
        qbtn.setToolTip("Нажмите для кнопки для выхода.")
        qbtn.clicked.connect(self._quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(350, 400)

        self.resize(450, 450)
        self.center()
        self.setWindowTitle("app")
        self.setWindowIcon(QIcon("web.png"))

        self.show()

    def _generate_keys(self):
        json_data = self.read_json_file(os.path.abspath(os.getcwd()) + PATH)
        if json_data:
            symmetric_key = json_data.get("symmetric_key", "")
            public_key = json_data.get("public_key", "")
            secret_key = json_data.get("secret_key", "")
        if symmetric_key and public_key and secret_key:
            task.generate_keys(symmetric_key, public_key, secret_key, 16)

    def _encrypt(self):
        json_data = self.read_json_file(os.path.abspath(os.getcwd()) + PATH)
        if json_data:
            symmetric_key = json_data.get("symmetric_key", "")
            public_key = json_data.get("public_key", "")
            secret_key = json_data.get("secret_key", "")
        if symmetric_key and public_key and secret_key:

    def _decrypt(self):
        return

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
