from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QMessageBox,QRadioButton,QHBoxLayout,QVBoxLayout

app = QApplication([])
main_window = QWidget()
text = QLabel("Як звали першого ютуб-блогера, який набрав 100000000 підписників?")
button = QRadioButton("PewDiePie")
button2 = QRadioButton("Рет і Лінк")
button3 = QRadioButton("SlivkiShow")
button4 = QRadioButton("TheBrianMaps")
button5 = QRadioButton("Mister Max")
button6 = QRadioButton("EeOneGuy")


line = QVBoxLayout()


hline = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()



hline.addWidget(text,alignment=Qt.AlignCenter)

hline2.addWidget(button, alignment=Qt.AlignCenter)
hline3.addWidget(button2, alignment=Qt.AlignCenter)
hline2.addWidget(button4, alignment=Qt.AlignCenter)
hline3.addWidget(button3, alignment=Qt.AlignCenter)

hline2.addWidget(button5, alignment=Qt.AlignCenter)
hline3.addWidget(button6, alignment=Qt.AlignCenter)


line.addLayout(hline)
line.addLayout(hline2)
line.addLayout(hline3)

def win():
    victory = QMessageBox()
    victory.setText("Ви виграли 2 копійки")

    victory.exec_()
def lose():
    victory = QMessageBox()
    victory.setText("Ви програли хату!")
    victory.exec_()
#a = """
#background-color : yellow;
#font-size: 20px
#"""

#button.setStyleSheet(a)
button.clicked.connect(win)
button2.clicked.connect(lose)
button3.clicked.connect(lose)
button4.clicked.connect(lose)
button5.clicked.connect(lose)
button6.clicked.connect(lose)



main_window.setLayout(line)

main_window.show()
app.exec_()
