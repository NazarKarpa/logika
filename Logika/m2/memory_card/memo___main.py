from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle  # перемішуватимемо відповіді у картці питання

from memo___card_layout import *
from memo___main_layout import *
from memo___edit_layout import *
from memo___data import *

main_width, main_height = 1000, 450  # початкові розміри головного вікна
card_width, card_height = 600, 500  # початкові розміри вікна "картка"
time_unit = 60000


radio_list = [Butoonr1,Butoonr2,Butoonr3,Butoonr4]

questions_listmodel = QuestionListModel()  # список запитань
# запам'ятовуємо, що у формі редагування питання з чим пов'язано
frm_edit = QuestionEdit(0, txt_Question, txt_Answer,
                        txt_Wrong1, txt_Wrong2, txt_Wrong3)
frm_card = 0  # тут буде зв'язуватися питання з формою тесту
timer = QTimer()
win_main = QWidget()
win_card = QWidget()

win_main.setStyleSheet('''
                        background-color: black;
                        color: white;
                        border: 1px solid green
                        ''')
win_card.setStyleSheet('''
                        background-color: black;
                        color: white;
                        border: 1px solid yellow;
                        font-size: 20px;
                        ''')
btn_delete.setStyleSheet('''
                         background-color: red;   
                         ''')
btn_add.setStyleSheet('''
                         background-color: green;   
                         ''')

Lb_result.setStyleSheet("margin: 35px")
# Тестові данні
def testlist():

    frm = Question('Бетон важить 10 кг,скільки коштують кілограм апельсинів', '100 грам грошей', 'незнаю', 'знаю', '1 бетон')
    questions_listmodel.form_list.append(frm)
    frm = Question('Була 1 курка в тебе,2 курки привезли сусіду,скільке в тебе курей?', '1', '3', 'Сусід', '5')
    questions_listmodel.form_list.append(frm)
    frm = Question('Який матеріал використовується для виробництва найбільшої кількості одягу?', 'Бавовна', 'Шовк', 'Вовна', 'Поліестер')
    questions_listmodel.form_list.append(frm)
    frm = Question('Яка найвища гора в світі?', 'Еверест', 'Кіліманджаро', 'Маккінлі', 'Аконкагуа')
    questions_listmodel.form_list.append(frm)

# Функції для проведення тесту


def set_card():
    ''' задає, який вигляд має вікно картки'''
    win_card.resize(card_width, card_height)
    win_card.move(300, 300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layuot_card)


def set_main():
    ''' задає, який вигляд має основне вікно'''
    win_main.resize(main_width, main_height)
    win_main.move(100, 100)
    win_main.setWindowTitle('Список питань')
    win_main.setLayout(layot_main)


def sleep_card():
    ''' картка ховається на час, зазначений у таймері'''
    win_card.hide()
    timer.setInterval(time_unit * box_min.value())
    timer.start()


def show_card():
    ''' показує вікно (за таймером), таймер зупиняється'''
    win_card.show()
    timer.stop()


def show_random():
    ''' показати випадкове запитання '''
    global frm_card
    frm_card = random_AnswerCheck(questions_listmodel, lb_quastion, radio_list, Lb_correct, Lb_result)
    frm_card.show()
    show_question()


def click_OK():
    ''' перевіряє запитання або завантажує нове запитання '''
    if button.text() != 'Наступне питання':
        frm_card.check()
        show_result()
    else:
        # напис на кнопці дорівнює 'Наступний', ось і створюємо наступне випадкове запитання:
        show_random()


def back_to_menu():
    ''' повернення з тесту у вікно редактора '''
    win_card.hide()
    win_main.showNormal()

# Функції для редагування питань


def edit_question(index):
    ''' завантажує у форму редагування запитання і відповіді, що відповідають переданому рядку '''

    if index.isValid():
        i = index.row()
        frm = questions_listmodel.form_list[i]
        frm_edit.change(frm)
        frm_edit.show()


def add_form():
    ''' додає нове запитання і пропонує його змінити '''
    questions_listmodel.insertRows()
    last = questions_listmodel.rowCount(0) - 1

    index = questions_listmodel.index(last)
    list_questions.setCurrentIndex(index)
    edit_question(index)
    txt_Question.setFocus(Qt.TabFocusReason)


def del_form():
    ''' видаляє питання і перемикає фокус '''
    questions_listmodel.removeRows(list_questions.currentIndex().row())
    edit_question(list_questions.currentIndex())


def start_test():
    ''' на початку тесту форма зв'язується з випадковим питанням і показується '''
    show_random()
    win_card.show()
    win_main.showMinimized()

# Встановлення потрібних з`єднань


def connects():
    list_questions.setModel(questions_listmodel)
    list_questions.clicked.connect(edit_question)
    btn_add.clicked.connect(add_form)
    btn_delete.clicked.connect(del_form)
    btn_start.clicked.connect(start_test)
    button.clicked.connect(click_OK)
    buttonmenu.clicked.connect(back_to_menu)
    timer.timeout.connect(show_card)
    buttonslip.clicked.connect(sleep_card)


testlist()
set_card()
set_main()
connects()
win_main.show()
app.exec_()
