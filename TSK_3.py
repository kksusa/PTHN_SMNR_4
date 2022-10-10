import random

def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def Polynomial(k):
    expression = ""
    for i in range(k, -1, -1):
        coefficient = str(random.randrange(100))
        if coefficient == "0": continue
        elif i == 1: expression += coefficient + "x+"
        elif i == 0: expression += coefficient
        else: expression += coefficient + "x^" + str(i) + "+"
    return expression

expression = Polynomial(CheckNumbers("Введите максимальную степень многочлена:"))
print(f"Сгенерирован многочлен: {expression}")