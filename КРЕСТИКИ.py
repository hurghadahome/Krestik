import random

m = [
        "|",
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        "|---|---|---|",
        "============="
    ]
# m консоль для игры

def nax(d):
    if d != "O":
        if d != "X":
            if d != str:
                if d != "|":
                    if d != "|---|---|---|":
                        if d != "=============":
                            return True
    else:
        return False
# разметка для  функциеи filter с последующей раздачей случайных чисел random.choice

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [7, 5, 3]]
# счастивые сочетания индексов для победы или поражения

def viv():
    for i in m1:
        cc = 0
        for p in i:
            if m[p] == "X":
                cc += 1
            if cc == 3:
                return True
    else:
        return False
   # победа

def bad():
    for k in m1:
        ccc = 0
        for h in k:
            if m[h] == "O":
                ccc += 1
            if ccc == 3:
                return True
    else:
        return False
   # поражение

def patt():
    for i in range(len(m)):
        p = 0
        if m[i] == int:
            p += 1
            if p == 0:
                return True
    else:
        return False
   # в случае пата


def play():
# основная функция игры
    print(f"{m[11]}\n"
          f"{m[0]} {m[1]} {m[0]} {m[2]} {m[0]} {m[3]} {m[0]}"
          f"\n"
          f"{m[10]}\n"
          f"{m[0]} {m[4]} {m[0]} {m[5]} {m[0]} {m[6]} {m[0]}"
          f" \n"
          f"{m[10]}\n"
          f"{m[0]} {m[7]} {m[0]} {m[8]} {m[0]} {m[9]} {m[0]}"
          f" \n"
          f"{m[11]}")
    n = int(input("ВВЕДИТЕ ЧИСЛО ГДЕ БУДЕТ СТОЯТЬ X:"))
    # консоль


    if m[n] == "O":
        print("ТЫ НЕ ПРАВИЛЬНО ВВЕЛ ЧИСЛО!!!")
        play()
    elif m[n] == "X":
        print("ТЫ НЕ ПРАВИЛЬНО ВВЕЛ ЧИСЛО!!!")
        play()
   # защита от дурака

    for i in range(len(m)):
        if i == n:
            m[i] = "X"
   # ход игрока

    if viv() == True:
        print("<---------------------->\n"
              "<-----ВЫ ПОБЕДИЛИ!----->\n"
              "<----ИГРА ОКОНЧЕНА!---->")
        play()
    # если победа человека

    m[random.choice(list(filter(nax, m)))] = "O"
    play()
    # ход машины

    if bad() == True:
        print("<------------------------->\n"              
              "ТЫ ПРОИГРАЛ ГЛУПЫЙ ЧЕЛОВЕК!\n"
                "<-----ИГРА ОКОНЧЕНА!---->")
        play()
    # если победа машины

    if patt() == True:
        print("<------------------------->\n"
              "           НИЧЬЯ!         \n"
                "<-----ИГРА ОКОНЧЕНА!---->")
        play()
    # в случае пата
    else:
         play()
    # если никто не победил продолжаем игру

play()
# функция запущена