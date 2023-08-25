from PyQt5.QtWidgets import QWidget
from random import randint, shuffle


class Quastion():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answere3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answere3 = wrong_answere3

    def got_wrong(self):
        print("Ця відповідь не правельна")

    def got_right(self):
        print("Ця відповідь правельна")
class QuestionViev():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answere3):
        self.frm_model = frm_model
        self.quastion = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answere3 = wrong_answere3
    def show(self):
        self.quastion.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answere3.setText(self.frm_model.wrong_answere3)


