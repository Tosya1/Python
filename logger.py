from datetime import datetime as dt

def log_strike (player, mark, strike):
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open ('log.csv', 'a', encoding="utf8") as file:
        file.write(f'{time}; {player} поставил "{mark}" в ячейку {strike}\n')

def log_start (player, mark):
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open ('log.csv', 'a', encoding="utf8") as file:
        file.write(f'{time}; По результатам жеребьевки {player} начинает игру с "{mark}"\n')

def log_win (player):
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open ('log.csv', 'a', encoding="utf8") as file:
        file.write(f'{time}; {player} побеждает в игре.\n')

def log_draw ():
    time = dt.now().strftime('%d.%m.%Y %H:%M:%S')
    with open ('log.csv', 'a', encoding="utf8") as file:
        file.write(f'{time}; Игра закончилась вничью.\n')