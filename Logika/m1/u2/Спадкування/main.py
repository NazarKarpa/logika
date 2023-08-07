
class Widhet:
    def __init__(self,text,x,y):
        self.text = text
        self.x = x
        self.y = y


    def druk(self):
        print("Напис:",self.text)
    def druk2(self):
        print(self.text)
    def druk3(self):
        print(self.text)

    def druk4(self):
        print('Розташування',self.x,self.y)




class Button(Widhet):

    def click(self,):
        dear.druk2()
        click = True

    def folse(self):
        dar.druk3()



dear = Button("Ви записані",100,100)
dar = Button("а шкода",100,100)
der = Widhet("розташовання",100,100)
dwar = Widhet("Брати учать на шоколадку 10 річну?",100,100)
dwar.druk()

der.druk4()
a = input("Хочете зареєструватися? Так-Не")

if a == "Так":
    dear.click()

else:
    dar.folse()


