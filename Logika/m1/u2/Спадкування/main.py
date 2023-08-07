
class Widhet:
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y


    def druk(self):
        print("Напис:",self.text)
        print("Координати",self.y,self.x)





class Button(Widhet):
    def __init__(self,text,x,y,is_clicked):
        super().__init__(text,x,y)
        self.is_clicked = is_clicked
        is_clicked = False






dear = Button("Ви записані",100,100)

der = Widhet("розташовання",100,100)
dwar = Widhet("Брати учать на шоколадку 10 річну?",100,100)


a = input("Хочете зареєструватися? Так-Не")

if a == "Так":


else:




