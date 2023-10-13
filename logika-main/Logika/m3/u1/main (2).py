import time

start_time = time.time ()
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

with open("students_large.txt", "r", encoding="utf-8") as files:
    datas = files.read()
    print(datas)
a = len(students)
b = 0





for i in students:
    b = b + i.great

    if i.great == 5:
        print("Найкращі учні:", i.surname)

abad = b / a

print(abad)





print("Поточний час роботи", time.time() - start_time)

