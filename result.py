def check_win (board):
    for i in board:
        if i[0] == i[1] == i[2]:
            return True

def check_draw(board, marks):
    list1 = [ marks[0] in i and marks[1] in i for i in board ]
    return False in list1

