def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def MinCommonMultiple(a, b):
    if a == b: return a
    else:
        if a < b:
            if b % a == 0: return b
            else:
                arrayB = []
                for i in range(1, a + 1):
                    arrayB.append(b * i)
                for i in range(1, b + 1):
                    check = a * i
                    if check in arrayB: break
        else:
            if a % b == 0: return a
            else:
                arrayA = []
                for i in range(1, b + 1):
                    arrayA.append(a * i)
                for i in range(1, a + 1):
                    check = b * i
                    if check in arrayA: break
    return check

a = CheckNumbers("Введите первое натуральное число:")
b = CheckNumbers("Введите второе натуральное число:")
print(f"НОК чисел {a} и {b} равен {MinCommonMultiple(a, b)}.")