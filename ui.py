def get_players ():
    player1 = input('Игрок1, введите Ваше Имя: ')
    player2 = input('Игрок2, введите Ваше Имя: ')
    players = [player1, player2]
    return players

def get_board ():
    board = [[3*i + 1, 3*i + 2, 3*i + 3] for i in range(3)]
    board.extend([[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]])
    return board


