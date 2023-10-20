import os

# потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap  # оптимізована для показу на екрані картинка
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel,
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
)

#from PIL import Image, ImageFilter
#from PIL.ImageQt import ImageQt  # Для перенесення графіки з Pillow до QT
#from PIL.ImageFilter import SHARPEN

app = QApplication([])
main_window = QWidget()

List = QListWidget()

button_folder = QPushButton("Папка")
button_left = QPushButton("Вліво")
button_right = QPushButton("Вправо")
button_flip = QPushButton("Джеркалоо")
button_sharp = QPushButton("Різкість")
button_bw = QPushButton("Ч.Б")

lst_files = QListWidget()

Photo = QLabel("Картинка")


layouth1 = QHBoxLayout()
layoutv1 = QVBoxLayout()
layouth2 = QHBoxLayout()
layoutv2 = QVBoxLayout()

layoutv1.addWidget(button_folder)
layoutv1.addWidget(lst_files)
layouth1.addWidget(button_left)
layouth1.addWidget(button_right)
layouth1.addWidget(button_flip)
layouth1.addWidget(button_sharp)
layouth1.addWidget(button_bw)

layoutv2.addWidget(Photo)
layoutv2.addLayout(layouth2)

layouth2.addLayout(layoutv1, 1)
layouth2.addLayout(layoutv2, 4)

main_window.setLayout(layouth2)



main_window.show()
app.exec_()