
class Widhet:
    def __init__(self,text,x,y,):
        self.text = text
        self.x = x
        self.y = y

    def druk(self):
        e = ("брати участь?")
        a = (x,y)




class Button(Widhet):
    x = None
    y = None
    def click(self,text):
        self.text = text
d = Button("А жаль")
b = Widhet("ви уже записаний")
x = 100
Button.x = 100
Button.y = 100

print("Розташовання",Button.x,"на",Button.y)
a = input("Так-Не")

if a == "Так":
    print(b)
else:
    print(d)

