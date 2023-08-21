from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
app = QApplication([])
button = QPushButton("Відповісти")
buttonslip = QPushButton("Відпочити")
buttonmenu = QPushButton("Меню")


lb_quastion = QLabel("")
box_min = QSpinBox()
box_min.setValue(5)

RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()
Butoonr1 = QRadioButton('')
Butoonr2 = QRadioButton('')
Butoonr3 = QRadioButton('')
Butoonr4 = QRadioButton('')

RadioGroup.addButton(Butoonr1)
RadioGroup.addButton(Butoonr2)
RadioGroup.addButton(Butoonr3)
RadioGroup.addButton(Butoonr4)

layuot_ans1 = QHBoxLayout()
layuot_ans2 = QVBoxLayout()
layuot_ans3 = QVBoxLayout()



layuot_ans2.addWidget(Butoonr1)
layuot_ans2.addWidget(Butoonr2)


layuot_ans3.addWidget(Butoonr3)
layuot_ans3.addWidget(Butoonr4)

layuot_ans1.addLayout(layuot_ans2)
layuot_ans1.addLayout(layuot_ans3)
RadioGroupBox.setLayout(layuot_ans1)

AnsGroupBox = QGroupBox()
Lb_result = QLabel("")
Lb_correct = QLabel("")

layuot_res = QVBoxLayout()
layuot_res.addWidget(Lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layuot_res.addWidget(Lb_correct,alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layuot_res)

AnsGroupBox.hide()

layuot_card = QVBoxLayout()
layuot_line1 = QHBoxLayout()
layuot_line2 = QHBoxLayout()
layuot_line3 = QHBoxLayout()
layuot_line4 = QHBoxLayout()

layuot_line1.addWidget(buttonmenu)
layuot_line1.addStretch(1)
layuot_line1.addWidget(buttonslip)
layuot_line1.addWidget(box_min)
layuot_line1.addWidget(QLabel("Хвилин"))

layuot_line2.addWidget(lb_quastion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layuot_line3.addWidget(RadioGroupBox)
layuot_line3.addWidget(AnsGroupBox)

layuot_line4.addStretch(1)
layuot_line4.addWidget(button)
layuot_line4.addStretch(1)
layuot_card.addLayout(layuot_line1)
layuot_card.addLayout(layuot_line2)
layuot_card.addLayout(layuot_line3)
layuot_card.addLayout(layuot_line4)









# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass
