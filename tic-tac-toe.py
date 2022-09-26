import random


def Print_Board(board):
    print("┌───┬───┬───┐")

    print("│ " + board[1] + " │ " + board[2] + " │ " + board[3] + " │" + "       7 8 9")

    print("├───┼───┼───┤")

    print("│ " + board[4] + " │ " + board[5] + " │ " + board[6] + " │" + "       4 5 6")

    print("├───┼───┼───┤")

    print("│ " + board[7] + " │ " + board[8] + " │ " + board[9] + " │" + "       1 2 3")

    print("└───┴───┴───┘")


def User_Input(board):
    ans = input("Enter the number: ")
    if ans not in "1 2 3 4 5 6 7 8 9".split():
        print("Error 01 - 잘못된 입력입니다.")
        ans = User_Input(board)
    return int(ans)


def Board_Update(board, index, letter):
    board[index] = letter


def Blank(board, index):
    return board[index] == ' '


def Board_Copy(board):
    lst = []
    for i in board:
        lst.append(i)
    return lst


def Computer_Choose(board):
    for i in range(1, 10):
        copy = Board_Copy(board)
        if Blank(copy, i):
            Board_Update(copy, i, '○')
            if Judgment(copy, '○'):
                return i
    for i in range(1, 10):
        copy = Board_Copy(board)
        if Blank(copy, i):
            Board_Update(copy, i, '●')
            if Judgment(copy, '●'):
                return i
    point = Computer_Choose_Random(board, [1, 3, 7, 9])
    if point != None:
        return point
    elif board[5] == ' ':
        return 5
    return Computer_Choose_Random(board, [2, 4, 6, 8])


def Computer_Choose_Random(board, info):
    lst = []
    for i in info:
        if Blank(board, i):
            lst.append(i)
    if len(lst) > 0:
        return random.choice(lst)
    else:
        return None


def Judgment(board, letter):
    return ((board[1] == board[2] == board[3] == letter) or
            (board[4] == board[5] == board[6] == letter) or
            (board[7] == board[8] == board[9] == letter) or
            (board[1] == board[4] == board[7] == letter) or
            (board[2] == board[5] == board[8] == letter) or
            (board[3] == board[6] == board[9] == letter) or
            (board[1] == board[5] == board[9] == letter) or
            (board[3] == board[5] == board[7] == letter))


if __name__ == "__main__":
    i = 0
    board = [' '] * 10
    while i < 10:
        Print_Board(board)
        Board_Update(board, User_Input(board), '●')
        if Judgment(board, '●'):
            print("Player Win")
            break
        i += 1
        if i == 9:
            Print_Board(board)
            print("Game Tie!")
            break
        Board_Update(board, Computer_Choose(board), '○')
        if Judgment(board, '○'):
            Print_Board(board)
            print("Computer Win")
            break
        i += 1
