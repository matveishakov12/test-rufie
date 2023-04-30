from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)
from instr import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super()__init__()
        self.set.appear()
        self.initUI()
        self.connect()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y_)
    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction_text = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.yayout = QVBoxLayout()
        self.yayout.addWidget(self.hello_text)
        self.yayout.addWidget(self.instruction)
        self.yayout.addWidget(self.button)