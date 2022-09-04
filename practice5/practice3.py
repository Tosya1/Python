# Создайте программу для игры в ""Крестики-нолики"".
from random import choice

players = ['Player1', 'Player2']
marks = ['X', 'O']
board = [[3*i + 1, 3*i + 2, 3*i + 3] for i in range(3)]
board.extend([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])

def draw_board (board = board):
    for i in range(3):
        print('-------------')
        print(f'| {board[i][0]} | {board[i][1]} | {board[i][2]} |')
    print('-------------')
draw_board()

def check_win (board = board):
    for i in board:
        if i[0] == i[1] == i[2]:
            return True

def check_draw(board = board, marks = marks):
    list1 = [ marks[0] in i and marks[1] in i for i in board ]
    return False in list1

def tic_tac_toe (players = players, marks = marks, board = board):
    player = choice(players)
    mark = choice(marks)
    strikes = []
    count = 0
    print(f'{player} начинает игру с {mark}.')
    while check_win() != True:
        strike = int(input(f'{player}, введите номер ячейки для {mark} от 1 до 9: '))
        if strike in strikes:
            print(f'Ячейка{strike} уже занята')
        elif strike > 9 or strike < 1:
            print(f'Номер ячейки должен быть в диапазоне от 1 до 9')
        else:
            for i in board:
                for j in i:
                    if j == strike:
                        i[i.index(j)] = mark
            draw_board()
            player = players[players.index(player) -1]
            mark = marks[marks.index(mark) -1]
            strikes.append(strike)
            count += 1
            if check_win() == True:
                print(f'Победил {player}!')
            elif check_draw() != True:
                print('Ничья!')
                break

tic_tac_toe(players, marks, board)

