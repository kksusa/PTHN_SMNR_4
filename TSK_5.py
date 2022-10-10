import random
import json
import time
from os import system

def CheckNumbers(param):
    while True:
        number = input(f"{param}")
        if number == "": return number
        else:
            try:
                number = int(number)
                if number > 0: return number
                else: print("Число введено неправильно.")
            except:
                print("Число введено неправильно.")

def Joke():
    j1 = """Жена посылает мужа-программиста в магазин: 
- Купи батон колбасы. Да, и спроси, есть ли яйца. Если есть - возьми десяток. 
Программист приходит в магазин: 
- Батон колбасы, пожалуйста. Ага, спасибо. А яйца у вас в продаже есть? 
- Есть. 
- Тогда, пожалуйста, ещё девять батонов колбасы :)"""
    j2 = """Если бы программисты были врачами, им бы говорили «У меня болит нога»,
а они отвечали «Ну не знаю, у меня такая же нога, а ничего не болит» :)"""
    j3 = "Жил-был программист и было у него два сына - Антон и Неантон :)"
    j4 = """Российские программисты создали аналог известной программы "Окей, Google!" под названием
"Окей, Х*й!", потому что в России последний знает намного больше, чем Google :)"""
    j5 = """Приходит студент-программист на занятия с утра злой. Его одногрупники спрашивают:
- Ты чего такой злой?
- Да программу вчера всю ночь набивал.
- И что, не заработала?
- Да нет, заработала.
- Может, неправильно заработала?
- Да нет, правильно.
- А что тогда?
- Да на Backspace уснул...  :)"""
    j6 = """Из жизни программистов:
Премия в 12000$ была выплачена вчера хакеру, научившемуся сохраняться в «Сапере» :)"""
    j7 = """Просыпается программист с большого бодуна, поворачивается, а рядом какая-то девушка лежит.
- Оорs, обнаружено новое устройство... :)"""
    j8 = """Программист ставит себе на тумбочку перед сном два стакана. 
Один с водой - на случай, если захочет ночью пить. 
А второй пустой - на случай, если не захочет :)"""
    return random.choice([j1, j2, j3, j4, j5, j6, j7, j8])

def AddCharacteristics(array):
    movie = []; name = ""; cast = []; similiar = []
    name = input("Введите название фильма: ")
    if name == "":
        print("Вы не ввели название фильма.\nЧто ж, давайте введём другую команду:")
        return
    else: 
        for k in range(len(array)):
            if name.lower() in (array[k][0]).lower():
                similiar.append(array[k])
        if similiar != []:
            print("\nПо-моему, такой фильм уже есть. Посмотрите, что я нашёл:\n")
            time.sleep(1)
            ListMovies(similiar)
            while True:
                answer = (input("Вашего фильма точно нет в списках (есть/нет)?\n")).lower()
                if answer == "есть":
                    break
                elif answer == "нет":
                    break
                else:
                    print('Введите "есть" или "нет".')
                    continue
            if answer == "есть":
                print("Что ж, давайте введём другую команду...")
                return
            else: print("\nОтлично! Тогда продолжаем...\n") 
        movie.append(name)
        print("\nДавайте еще чего-нибудь заполним о нём.\n")
        movie.append(input("Введите жанр фильма: "))
        movie.append(CheckNumbers("Введите год выхода фильма: "))
        movie.append(input("Введите режиссёра фильма: "))
        movie.append(input("Введите оператора-постановщика фильма: "))
        movie.append(input("Введите композитора фильма: "))
        movie.append(input("Введите продюсера фильма: "))
        i = 1
        while True:
            castName = input(f"Введите {i}-го актёра главной роли: ")
            if castName == "":
                movie.append(cast)
                break
            else:
                cast.append(castName)
                while True:
                    answer = input("Ещё есть актеры (да/нет)?\n")
                    if answer.lower() == "да":
                        i += 1
                        break
                    elif answer.lower() == "нет":
                        break
                    else:
                        print('Введите "да" или "нет".')
                        continue
            if answer == "нет":
                movie.append(cast)
                break
            else: continue
    return movie

def ReadMovie():
    with open("kinobot.json") as movieDB:
        array = json.load(movieDB)
    return array

def SaveMovie(array):
    with open("kinobot.json", "w", encoding = "utf-8") as movieDB:
        movieDB.write(json.dumps(array, ensure_ascii = False))
        movieDB.close()
        
def DeleteMovie(array):
    similiar = []
    actors = ""
    params = ["Название фильма:         ",
              "Жанр:                    ",
              "Год выхода:              ",
              "Режиссёр:                ",
              "Оператор-постановщик:    ",
              "Композитор:              ",
              "Продюсер:                ",
              "В главных ролях:         "]
    if array == []: print("В КиноБоте ничего нет :(\nМожет, стоит, что-то добавить через /add?")
    else:
        result = False
        choice = input("Напишите часть или полное название фильма, который хотите удалить из КиноБота:\n")
        if choice == "":
            print("Понятненько...")
            time.sleep(0.5)
            return array
        for p in range(len(array)):
            if choice.lower() in (array[p][0]).lower():
                similiar.append(p)
        if similiar == []:
            print("\nЧто-то нет таких фильмов.\n\nПроверьте список фильмов через /list.")
            return array
        elif len(similiar) > 1:
            print("\nПосмотрите, сколько таких фильмов я нашёл:\n")
            for i in range(len(similiar)):
                time.sleep(0.5)
                print(f"{i + 1} фильм:\n")
                for j in range(len(array[similiar[i]]) - 1):
                    print(f"{params[j]} {str(array[similiar[i]][j]).title()}")
                for k in range(len(array[similiar[i]][7])):
                    actors = actors + str(array[similiar[i]][7][k]).title() + ", "
                actors = actors[:-2]
                print(f"{params[7]} {actors}\n")
                actors = ""
            while True:
                try:
                    number = int(input("Выберите номер фильма, который хотите удалить: "))
                    if number < 1 or number > len(similiar):
                        print("Вы ввели неправильный номер.")
                    else: break
                except:
                    print("Вы ввели не число.")
        if len(similiar) == 1: number = 0
        while True:
            answer = input(f'Вы действительно хотите удалить фильм "{array[similiar[number - 1]][0]}" (да/нет)?\n')
            if answer.lower() == "да":
                print(f'Фильм "{array[similiar[number - 1]][0]}" удалён из КиноБота.')
                array.pop(similiar[number - 1])
                return array
            elif answer.lower() == "нет":
                print("Ничего не удалено.")
                return array
                break
            else: print("Что-то я не могу понять ответ...")

def RandomMovie(array):
    chosen = []
    chosen.append(random.choice(array))
    print("\nАхалай-Махалай, Ляськи-Масяськи...\n")
    time.sleep(1)
    ListMovies(chosen)

def ListMovies(array):
    actors = ""
    params = ["Название фильма:         ",
              "Жанр:                    ",
              "Год выхода:              ",
              "Режиссёр:                ",
              "Оператор-постановщик:    ",
              "Композитор:              ",
              "Продюсер:                ",
              "В главных ролях:         "]
    for i in range(len(array)):
        for j in range(len(array[i]) - 1):
            print(f"{params[j]} {str(array[i][j]).title()}")
        for u in range(len(array[i][7])):
            actors = actors + str(array[i][7][u]).title() + ", "
        actors = actors[:-2]
        print(f"{params[7]} {actors}")
        actors = ""
        print()

def EditMovie(array):
    similiar = []
    actors = ""
    params = ["Название фильма:         ",
              "Жанр:                    ",
              "Год выхода:              ",
              "Режиссёр:                ",
              "Оператор-постановщик:    ",
              "Композитор:              ",
              "Продюсер:                ",
              "В главных ролях:         "]
    if array == []: print("В КиноБоте ничего нет :(\nМожет, стоит, что-то добавить через /add?")
    else:
        choice = input("Напишите часть или полное название фильма, который хотите редактировать в КиноБоте:\n")
        if choice == "":
            print("Понятненько...")
            time.sleep(0.5)
            return array
        for p in range(len(array)):
            if choice.lower() in (array[p][0]).lower():
                similiar.append(p)
        if similiar == []:
            print("\nЧто-то нет таких фильмов.\n\nПроверьте список фильмов через /list.")
            return array
        elif len(similiar) > 1:
            print("\nПосмотрите, сколько таких фильмов я нашёл:\n")
            for i in range(len(similiar)):
                time.sleep(0.5)
                print(f"{i + 1} фильм:\n")
                for j in range(len(array[similiar[i]]) - 1):
                    print(f"{params[j]} {str(array[similiar[i]][j]).title()}")
                for k in range(len(array[similiar[i]][7])):
                    actors = actors + str(array[similiar[i]][7][k]).title() + ", "
                actors = actors[:-2]
                print(f"{params[7]} {actors}\n")
                actors = ""
            while True:
                try:
                    number = int(input("Выберите номер фильма, который хотите редактировать: "))
                    if number < 1 or number > len(similiar):
                        print("Вы ввели неправильный номер.")
                    else: break
                except:
                    print("Вы ввели не число.")
        while True:
            choice = input("\nНапишите часть или полное название параметра, который хотите редактировать:\n")
            if choice == "":
                print("Такого параметра нет.")
                continue
            else:
                result = ""
                for i in range(len(params)):
                    if choice.lower() in (params[i]).lower():
                        result = params[i].rstrip()
                        index = i
                if result != "": break
                else:
                    print("Такого параметра нет.")
                    continue
        if len(similiar) != 1: resultMeaning = array[similiar[number - 1]][index]
        else: resultMeaning = array[similiar[0]][index]
        if result != "В главных ролях:":
            if resultMeaning != "":
                resultMeaning = input(f'Параметр "{result.rstrip()}" имеет значение "{resultMeaning}".\nВведите новое значение: ')
            else: resultMeaning = input(f'Параметр "{result}" пустой.\nВведите новое значение: ')
        else:
            for l in resultMeaning:
                actors = actors + str(l).title() + ", "
            actors = actors[:-2]
            resultMeaning = actors
            if resultMeaning != "":
                print(f'Параметр "В главных ролях" имеет значение "{resultMeaning}".')
            else:
                print('Параметр "В главных ролях" пустой.')
            x = 1
            resultMeaning = []
            while True:
                castName = input(f"Введите {x}-го актёра главной роли: ")
                if castName == "":
                    break
                else:
                    resultMeaning.append(castName)
                    while True:
                        answer = input("Ещё есть актеры (да/нет)?\n")
                        if answer.lower() == "да":
                            x += 1
                            break
                        elif answer.lower() == "нет":
                            break
                        else:
                            print('Введите "да" или "нет".')
                            continue
                if answer == "нет":
                    break
        if len(similiar) != 1: array[similiar[number - 1]][index] = resultMeaning
        else: array[similiar[0]][index] = resultMeaning
        print("\nНовый параметр записан ;)")
        return array
        
system('clear')
print("\nДобро пожаловать в КиноБота!")
time.sleep(0.5)
print("\n#  #  #   #  #   #    ##    #####    ##    #####")
time.sleep(0.07)
print("# #   #  ##  #   #   #  #   #       #  #     #")
time.sleep(0.07)
print("##    # # #  #####  #    #  ####   #    #    #")
time.sleep(0.07)
print("# #   ##  #  #   #   #  #   #   #   #  #     #")
time.sleep(0.07)
print("#  #  #   #  #   #    ##    ####     ##      #")
time.sleep(0.5)
print("\nДля вызова списка возможных команд наберите /help.")
while True:
    cmd = input("/")
    movieDB = ReadMovie()
    if cmd == "help":
        print("""\nСписок возможных команд для реализации:
        
/add: Добавить фильм в базу данных;
/clear: Очистить базу данных КиноБота;
/cls: Очистить экран;
/delete: Удалить фильм из КиноБота;
/edit: Изменить данные о фильме;
/exit: Выйти из программы;
/help: Вывести список возможных команд;
/list: Вывести список всех фильмов;
/random: Вывести случайный фильм из КиноБота;

Введите команду:""")
    elif cmd == "add":
        movie = AddCharacteristics(movieDB)
        if movie != None:
            movieDB.append(movie)
            SaveMovie(movieDB)
            print("\nФильм записан в КиноБоте.\n\nВведите команду:")
    elif cmd == "clear":
        answer = input('\nВНИМАНИЕ! Эта команда удалит все фильмы из КиноБота!\nДля потдтверждения удаления наберите "да".\n')
        if answer.lower() == "да":
            array = []
            SaveMovie(array)
            print("\nТеперь КиноБот чист, как попа младенца.\n\nВведите команду:")
        else: print("\nНичего не удалено.\n\nВведите команду:")
    elif cmd == "cls":
        print("\nОчищаем экран:")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
        system('clear')
        print("Введите команду:")
    elif cmd == "delete":
        SaveMovie(DeleteMovie(movieDB))
        print("\nВведите команду:")
    elif cmd == "edit":
        SaveMovie(EditMovie(movieDB))
        print("\nВведите команду:")
    elif cmd == "exit":
        print("\nПока-пока...")
        time.sleep(1)
        print("\nПлак-плак :(")
        time.sleep(1)
        break
    elif cmd == "list":
        if movieDB != []:
            print("\nЧто мы имеем...\n")
            ListMovies(movieDB)
            print("Введите команду:")
        else: print("\nВ КиноБоте ничего нет :(\nМожет, стоит, что-то добавить через /add?")
    elif cmd == "random":
        RandomMovie(movieDB)
        print("Введите команду:")
    else: print(f"""\nХмм... Похоже, я не знаю такую команду...

Зато я знаю анекдот:\n\n{Joke()}

Что ж... Давайте попробуем снова...

Введите команду:""")