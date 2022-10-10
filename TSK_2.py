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

def GenerateList(number):
    array = []
    for i in range(number):
        array.append(random.randrange(10))
    return array

def NonRepeatingList(array):
    resultArray = []
    for i in array:
        count = 0
        for j in array:
            if j == i: count += 1
        if count == 1: resultArray.append(i)
    return resultArray

array1 = GenerateList(CheckNumbers("Введите число элементов в массиве:"))
print(f"Сгенерирован массив: {array1}")
print(f"Массив из неповторяющихся элементов: {NonRepeatingList(array1)}")