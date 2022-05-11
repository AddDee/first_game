field = "  1 2 3 \nA  | |  \n  -----\nB  | |  \n  -----\nC  | |  "
pos_moves = [["A1", 11], ["A2", 13], ["A3", 15],
             ["B1", 28], ["B2", 30], ["B3", 32],
             ["C1", 45], ["C2", 47], ["C3", 49]
             ]
winSteps = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
            ]
print(field)
step = 0
FirstStep = "X"
win = False


def getWin(string):
    return "X" in string


while not win:
    a = input("Введите ход: ")
    for i in range(0, 9):
        if not ("Введите ход" in pos_moves[i]):
            if a.upper() == pos_moves[i][0].upper():
                if FirstStep == "X":
                    field = field[0:pos_moves[i][1]] + "X" + field[(pos_moves[i][1] + 1):]
                    FirstStep = "0"
                    pos_moves[i] = "Введите ход"
                elif FirstStep == "0":
                    field = field[0:pos_moves[i][1]] + "0" + field[(pos_moves[i][1] + 1):]
                    FirstStep = "X"
                    pos_moves[i] = "Введите ход"
                print(field)
                step += 1
                for i in range(len(winSteps)):
                    if (pos_moves[winSteps[i][0]] == "X" and pos_moves[winSteps[i][1]] == "X" and
                            pos_moves[winSteps[i][2]] == "X"):
                        print(" Крестики выиграли!")
                        win = True;
                        break
                for i in range(len(winSteps)):
                    if (pos_moves[winSteps[i][0]] == "NULL" and pos_moves[winSteps[i][1]] == "NULL" and
                            pos_moves[winSteps[i][2]] == "NULL"):
                        print(" Нолики выиграли!")
                        win = True
                        break
                if step == 9:
                    print("Возможные ходы закончились.")
                    win = True
                    break

