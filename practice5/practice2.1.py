# Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг 
#после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не 
#более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
#конкурента?

from secrets import choice

def candy_game (bank, max_strike, players):
    player = choice(players)
    while bank > 0:
        bid = int(input(f'{player}, введите число конфет от 1 до 28: '))
        if bid > max_strike or bid <= 0:
            print('За один ход можно забрать не более, чем 28 и не менее, чем 1 конфету')
        elif bid > bank:
            print(f'Осталось всего {bank} конфет')           
        else: 
            bank -= bid
            print(f'Осталось {bank} кофет')
            if bank == 0:
                print(f'{player} выиграл и получает все конфеты :)')
            player = ''.join([i for i in players if i != player])

candy_bank = 2022
candy_max = 28
players = ['Player1', 'Player2']
candy_game(candy_bank, candy_max, players)