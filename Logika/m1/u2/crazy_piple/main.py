from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QMessageBox,QRadioButton,QHBoxLayout

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

hline.addWidget()

line.addLayout(hline)
line.addLayout(hline2)
line.addLayout(hline3)


main_window.setLayout(line)
main_window.setLayout(hline)
main_window.show()
app.exec_()
