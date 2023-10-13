from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from random import randint

app = QApplication([])
main_window = QWidget()

text = QLabel("Натисни щоб дізнатись у кого буде понос")
winner = QLabel("?")
button = QPushButton("Тикай!")

line = QVBoxLayout()
line.addWidget(text)
line.addWidget(winner)
line.addWidget(button)

def win():
    ran = randint(1, 20)
    winner.setText(str(ran))
button.clicked.connect(win)

main_window.setLayout(line)

main_window.show()
app.exec_()

