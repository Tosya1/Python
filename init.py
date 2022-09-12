from random import choice
import ui

players = ui.get_players()
board = ui.get_board()
marks = ['X', 'O']

def draw_board (board):
    for i in range(3):
        print('-------------')
        print(f'| {board[i][0]} | {board[i][1]} | {board[i][2]} |')
    print('-------------')

def toss_player (players):
        player = choice(players)
        return player

def toss_mark (marks):
        mark = choice(marks)
        return mark




