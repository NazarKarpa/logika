from memo___card_layout import*
from PyQt5.QtWidgets import QWidget
from random import shuffle

card_width, card_height = 600, 500 # початкові розміри вікна "картка"

def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка, чи вибрана правильна відповідь
    якщо відповідь була вибрана, то напис "правильно/не правильно" отримує потрібне значення
    і показує панель відповідів'''
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.setLayout(layuot_card)

win_card.show()
app.exec_()
