def CheckNumbers(param):
    while True:
        try:
            number = int(input(f"{param} "))
            if number > 0:
                return number
            else: print("Число введено неправильно.")
        except:
            print("Число введено неправильно.")

def PrimeFactor(number):
    array = []
    for i in range(2, number + 1):
        if number % i == 0:
            check = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    check = False
                    break
            if check == False: continue
            else: array.append(i)
    return array   

number = CheckNumbers("Введите любое натуральное число:")
if number == 1: print("У числа 1 нет простых множителей.")
else:
    factorList = PrimeFactor(number)
    print(f"Список простых множителей этого числа: {factorList}.")