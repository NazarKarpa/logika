from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox,QRadioButton,QHBoxLayout,QVBoxLayout

app = QApplication([])
main_window = QWidget()
text = QLabel("Ти надів носочок без дірочки?")
button = QRadioButton("Так")
button2 = QRadioButton("Не")
button3 = QRadioButton("Можливо")
button4 = QRadioButton("Напевно")

line = QVBoxLayout()


hline = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()



hline.addWidget(text,alignment=Qt.AlignCenter)

hline2.addWidget(button, alignment=Qt.AlignCenter)
hline3.addWidget(button2, alignment=Qt.AlignCenter)
hline2.addWidget(button4, alignment=Qt.AlignCenter)
hline3.addWidget(button3, alignment=Qt.AlignCenter)



line.addLayout(hline)
line.addLayout(hline2)
line.addLayout(hline3)

def win():
    victory = QMessageBox()
    victory.setText("Ура роблакс")
    victory.exec_()
def lose():
    victory = QMessageBox()
    victory.setText("Швидко надів,без дірочки")
    victory.exec_()

button.clicked.connect(win)
button2.clicked.connect(lose)
button3.clicked.connect(win)
button4.clicked.connect(lose)



main_window.setLayout(line)

main_window.show()
app.exec_()
