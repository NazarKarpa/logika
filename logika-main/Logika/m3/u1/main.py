with open("Top.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)
a = input("Веди автора")
with open("Top.txt", "a", encoding="utf-8") as file:

    file.write(f"({a})")


    
