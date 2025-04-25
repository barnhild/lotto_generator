import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,QComboBox, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
import os

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class LottoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.result_label = None
        self.generate_button = None
        self.layout = None
        self.game_selector = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Loto Number Generator')
        self.resize(900, 400)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)


        self.game_selector = QComboBox(self)
        self.game_selector.addItems(['Powerball', 'Mega Millions'])
        self.game_selector.currentIndexChanged.connect(self.generate_numbers)
        self.layout.addWidget(self.game_selector)

        self.result_label = QLabel('Click to generate Powerball numbers!', self)
        self.result_label.setFont(QFont('Arial',12))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        self.generate_button = QPushButton('Generate Numbers', self)
        self.generate_button.clicked.connect(self.generate_numbers)
        self.generate_button.setFont(QFont('Arial',12))
        self.layout.addWidget(self.generate_button)

        # Copy to Clipboard button
        self.copy_button = QPushButton('Copy to Clipboard', self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setFont(QFont('Arial', 10))
        self.layout.addWidget(self.copy_button)

        self.setWindowIcon(QIcon(resource_path("loto.png"))) # Or use .ico if you prefer


        self.setLayout(self.layout)
        self.show()

    def generate_numbers(self):
        game = self.game_selector.currentText()

        if game == 'Powerball':
            white_balls = sorted(random.sample(range(1, 70), 5))
            special_ball = random.randint(1, 26)
            result = f"White Balls: {white_balls} | Powerball: {special_ball}"

        elif game == 'Mega Millions':
            white_balls = sorted(random.sample(range(1, 71), 5))
            special_ball = random.randint(1, 25)
            result  = f"White Balls: {white_balls} | Mega Millions: {special_ball}"

        else:
            result = "Unknown game selected."

        self.result_label.setText(result)

    def copy_to_clipboard(self):
        text = self.result_label.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LottoApp()
    sys.exit(app.exec_())

