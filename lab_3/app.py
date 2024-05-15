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

import cryptosystem
from constants import PATH


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cryptosystem = None
        QToolTip.setFont(QFont("SansSerif", 14))
        self.setToolTip("Это <b>QWidget</b> виджет")
        self.label = QLabel(self)
        self.label.setText("Привет пользователь!")
        self.label.adjustSize()
        self.label.move(200, 50)

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
        btn3.clicked.connect(self.generate_keys)
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
        self.resize(450, 450)
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
        return

    def create_by_user(self):
        return

    def generate_keys(self):
        return

    def encrypt_text(self):
        return

    def decrypt_text(self):
        return

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
