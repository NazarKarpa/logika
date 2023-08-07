
class Widhet:
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y


    def druk(self):
        print("Напис:",self.text)
        print("Координати",self.y,self.x)





class Button(Widhet):
    def __init__(self,text,x,y):
        super().__init__(text,x,y)

        self.is_clicked = False
    def click(self):
        self.is_clicked = True
        print("Ви записані")







adab = Button("Хочеш приняти участь?",100,100)

a = input("Хочете зареєструватися? Так-Не")

if a == "Так":
    adab.click()


else:
    print("а шкода")




