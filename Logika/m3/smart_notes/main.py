
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json

def writeToFile():
    with open("notes.json", "w", encoding="utf8") as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)


app = QApplication([])
window = QWidget()

field_text = QTextEdit()
lb_notes = QLabel("Список заміток")
lst_notes = QListWidget()
btn_note_create = QPushButton("Стровити замітку")
btn_note_del = QPushButton("Видалити замітку")
btn_note_save = QPushButton("Зберегти замітку")

lb_tags = QLabel("Список тегів")

lst_tags = QListWidget()

field_tag = QLineEdit()
btn_tags_add = QPushButton("Додати до замітки")
btn_tgs_del = QPushButton("Відкріпити від заміти")
btn_tags_search = QPushButton("Шукати замітки за тегом")


row1 = QHBoxLayout()

row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)

row2 = QHBoxLayout()


layout_notes = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

row2.addWidget(btn_tags_search)
row2.addWidget(btn_tgs_del)

col2.addWidget(btn_note_save)


col1.addWidget(field_text)

col2.addLayout(row1)
col2.addWidget(lb_tags)
col2.addWidget(lst_tags)
col2.addWidget(field_tag)

col2.addWidget(btn_tags_add)
col2.addLayout(row2)

def show_notes():
    key = lst_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['текст'])

    lst_tags.clear()
    lst_tags.addItems(notes[key]["теги"])
def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки")
    if note_name and ok:
        lst_notes.addItem(note_name)
        notes[note_name] = {"текст": "", "теги": []}
        writeToFile()

def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
    key = lst_notes.currentItem().text()
    del notes[key]
    writeToFile()

    field_text.clear()
    lst_tags.clear()
    lst_notes.clear()
    lst_notes.addItems(notes)

def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()


        notes[key]["текст"] = field_text.toPlainText()
        writeToFile()

btn_note_save.clicked.connect(save_note)

btn_note_del.clicked.connect(del_note)

btn_note_create.clicked.connect(add_note)



lst_notes.itemClicked.connect(show_notes)
with open("notes.json", "r", encoding="utf8") as file:
    notes = json.load(file)
lst_notes.addItems(notes)






window.setLayout(layout_notes)
window.show()
app.exec_()