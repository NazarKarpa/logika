class Student():
    def __init__(self, surname, name, great):
        self.surname = surname
        self.name = name
        self.great = great
students = []

with open("stoden.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split(" ")
        obj = Student(data[0], data[1], int(data[2]))
        students.append(obj)
for i in students:
    if i.great == 5:
        print(i.surname)
