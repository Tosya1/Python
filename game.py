import init as init
import logger as log
import result as res

def tic_tac_toe (players, marks, board):
    player = init.toss_player(players)
    mark = init.toss_mark(marks)
    strikes = []
    count = 0
    print(f'{player} начинает игру с {mark}.')
    init.draw_board(board)
    log.log_start(player, mark)
    while res.check_win(board) != True:
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
            init.draw_board(board)
            log.log_strike(player, mark, strike)
            player = players[players.index(player) -1]
            mark = marks[marks.index(mark) -1]
            strikes.append(strike)
            count += 1
            if res.check_win(board) == True:
                print(f'Победил {player}!')
                log.log_win(player)
            elif res.check_draw(board, marks) != True:
                print('Ничья!')
                log.log_draw()
                break
