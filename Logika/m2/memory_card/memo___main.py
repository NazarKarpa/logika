from memo___card_layout import*
from PyQt5.QtWidgets import QWidget
from random import shuffle
from memo___data import*

card_width, card_height = 600, 500 # початкові розміри вікна "картка"
radio_list = [Butoonr1,Butoonr2,Butoonr3,Butoonr4]

frm = Quastion("Яблуко","Апельсин","Огірок","Персик","Berry")
frm_card = QuestionViev(frm,lb_quastion,
radio_list[0],radio_list[1],radio_list[2],radio_list[3])

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
frm_card.show()
win_card.show()
app.exec_()
