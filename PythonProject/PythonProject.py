#Сначала, просто приветсвие пользователя
print("Добро пожаловать на игру Крестики и Нолики!")
print("Правилы простыe:\n\t1.выбирите фигуру\n\t2.После, выводите на консоль позицию которую хотите от 1-9\n\t3.Выиграет тот, у кого есть ряд фигуры")
print("Поехали!УДАЧНЫЙ ИГРЫ!\n")

#глобальные перемены
check_Figure_X = True #
check_Game = True
value = ["","","","","","","","",""]
users1_Figure = ""
users2_Figure = ""

#Функция: ввод от пользовотеля с выбором фигурки
def player_Input():
    global check_Figure_X
    global users1_Figure, users2_Figure
    while True:
      users1_Figure = input("Выбирайте фигуру, Х или О: ").upper()
      if users1_Figure == "X" or users1_Figure == "x":
         print("Вы выбрали фигуру Х, отличный выбор!\n")
         check_Figure_X = True
         users2_Figure = "O"
         break
      elif users1_Figure == "O" or users1_Figure == "o":
         print("Вы выбрали фигуру О, феноменальный выбор!\n")
         check_Figure_X = False
         users2_Figure = "X"
         break
      else:
         print("\n"*100)
         print("Вы вводили некоректный ответ, повторите.\nНапоминаю,только Х или О,")

#Функция:которая отвечает на процесс игры. Вывод игрового поле на экран, принимает поз.фигур 
def display_For_Game(positions_Value, users_Figure):
       global value
       if positions_Value == "1" and value[0] == "":
           value[0] = users_Figure
       elif positions_Value == "2" and value[1] == "":
            value[1] = users_Figure
       elif positions_Value == "3" and value[2] == "":
            value[2] = users_Figure
       elif positions_Value == "4" and value[3] == "":
            value[3] = users_Figure
       elif positions_Value == "5" and value[4] == "":
            value[4] = users_Figure
       elif positions_Value == "6" and value[5] == "":
            value[5] = users_Figure
       elif positions_Value == "7" and value[6] == "":
            value[6] = users_Figure
       elif positions_Value == "8" and value[7] == "":
            value[7] = users_Figure
       elif positions_Value == "9" and value[8] == "":
            value[8] = users_Figure
       else:
           pass
       print("\n" * 100)
       print(f" {value[6]}  || {value[7]} || {value[8]} \n ========== \n  {value[3]} || {value[4]} || {value[5]} \n ========== \n  {value[0]} || {value[1]} || {value[2]} \n")

def check_Win():
    check_Draw = 0
    global check_Game

    if value[0] == value[1] == value[2]!="":
        print(f"Игра закончился! Фигурка {value[0]} выиграла!")
        check_Game = False
    elif value[3] == value[4] == value[5]!="":
        print(f"Игра закончился! Фигурка {value[3]} выиграла!")
        check_Game = False
    elif value[6] == value[7] == value[8]!="":
        print(f"Игра закончился! Фигурка {value[6]} выиграла!")
        check_Game = False
    elif value[0] == value[3] == value[6]!="":
        print(f"Игра закончился! Фигурка {value[0]} выиграла!")
        check_Game = False
    elif value[1] == value[4] == value[7]!="":
        print(f"Игра закончился! Фигурка {value[1]} выиграла!")
        check_Game = False
    elif value[2] == value[5] == value[8]!="":
        print(f"Игра закончился! Фигурка {value[2]} выиграла!")
        check_Game = False
    elif value[0] == value[4] == value[8]!="":
        print(f"Игра закончился! Фигурка {value[0]} выиграла!")
        check_Game = False
    elif value[2] == value[4] == value[6]!="":
        print(f"Игра закончился! Фигурка {value[2]} выиграла!")
        check_Game = False
    else:
       for i in value:
          if i!="":
            check_Draw+=1
          if check_Draw == 9:
            print(f"Игра закончился! Ничья!")
            check_Game = False


#Функция: обьеденяют все функций, запускся игру
def start_Game():
    global check_Figure_X, users1_Figure, users2_Figure, check_Game, value
    player_Input()
    display_For_Game(0, "")
    while check_Game:
        check_Win()
        if check_Figure_X and check_Game:
           position = input("Введите позицию для Х: ")
           if users1_Figure == "X":
              display_For_Game(position, users1_Figure)
           else:
               display_For_Game(position, users2_Figure)
           check_Figure_X = False
        elif not check_Figure_X and check_Game:
           position = input("Введите позицию для O: ")
           if users2_Figure == "O":
              display_For_Game(position, users2_Figure)
           else:
              display_For_Game(position, users1_Figure)
           check_Figure_X = True
    else:
        result = input("Хотите играть еще?(1 - ДА  2 - НЕТ): ")
        if result == "1": 
            check_Game = True
            value = ["","","","","","","","",""]
            start_Game()
        elif result == "2":
            print("Спасибо за игру!")
            return
        else:
            return


start_Game()