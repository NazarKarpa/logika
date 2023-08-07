
class Widhet:
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y
        text = "Пон"

    def druk(self):
        print("Напис",text)
        print('Розташування',x,y)




class Button(Widhet):

    def click(self,click):
        click = True
        print("Ви записані")





a = input("Так-Не")

if a == "Так":
    click()

else:
    print("Мне пофек")


