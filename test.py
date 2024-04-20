def check_game_state(game):
    # check row
    for i in range(0,10):
        if game[i].count('X') > 4 or  game[i].count('O') :
            for j in range(0,6):
                if game[i][j] == game[i][j+1] and game[i][j] == game[i][j+2] and \
                    game[i][j] == game[i][j+3] and game[i][j] == game[i][j+4] and \
                    game[i][j] != ' ':
                    return True
    # check col
    for i in range(0,10):
        for j in range(0,6):
            if game[j][i] == game[j+1][i] and game[j][i] == game[j+2][i] and\
                game[j][i] == game[j+3][i] and game[j][i] == game[j+4][i] and\
                game[j][i] != ' ':
                return True
               
    
    for i in range(0,6):
        for j in range(0,5):
            if game[i][i] == game[i+1][i+1] and game[i][i] == game[i+2][i+2] and\
                game[i][i] == game[i+3][i+3] and game[i][i] == game[i+4][i+4] and\
                game[i][i] != ' ':
                return True
            if (j + 5 + i) < 10:
                if game[i][j+1+i] == game[i+1][j+2+i] and game[i][j+1+i] == game[i+2][j+3+i] and\
                    game[i][j+1+i] == game[i+3][j+4+i] and game[i][j+1+i] == game[i+4][j+5+i] and\
                    game[i][j+1+i] != ' ':
                    return True
                if game[j+1+i][i] == game[j+2+i][i+1] and game[j+1+i][i] == game[j+3+i][i+2] and\
                    game[j+1+i][i] == game[j+4+i][i+3] and game[j+1+i][i] == game[j+5+i][i+4] and\
                    game[j+1+i][i] != ' ':
                    return True
    for i in game:
        i.reverse()
    for i in range(0,6):
        for j in range(0,5):
            if game[i][i] == game[i+1][i+1] and game[i][i] == game[i+2][i+2] and\
                game[i][i] == game[i+3][i+3] and game[i][i] == game[i+4][i+4] and\
                game[i][i] != ' ':
                return True
            if (j + 5 + i) < 10:
                if game[i][j+1+i] == game[i+1][j+2+i] and game[i][j+1+i] == game[i+2][j+3+i] and\
                    game[i][j+1+i] == game[i+3][j+4+i] and game[i][j+1+i] == game[i+4][j+5+i] and\
                    game[i][j+1+i] != ' ':
                    return True
                if game[j+1+i][i] == game[j+2+i][i+1] and game[j+1+i][i] == game[j+3+i][i+2] and\
                    game[j+1+i][i] == game[j+4+i][i+3] and game[j+1+i][i] == game[j+5+i][i+4] and\
                    game[j+1+i][i] != ' ':
                    return True
    for i in game:
        i.reverse()
    return False

def final_state_score(game):
    for i in range(0,10):
            for j in range(0,6):
                if game[i][j] == game[i][j+1] and game[i][j] == game[i][j+2] and \
                    game[i][j] == game[i][j+3] and game[i][j] == game[i][j+4] and \
                    game[i][j] != ' ':
                    return 1 if game[i][j] == 'X' else -1
    # check col
    for i in range(0,10):
        for j in range(0,6):
            if game[j][i] == game[j+1][i] and game[j][i] == game[j+2][i] and\
                game[j][i] == game[j+3][i] and game[j][i] == game[j+4][i] and\
                game[j][i] != ' ':
                 return 1 if game[j][i] == 'X' else -1
               
    
    for i in range(0,6):
        for j in range(0,5):
            if game[i][i] == game[i+1][i+1] and game[i][i] == game[i+2][i+2] and\
                game[i][i] == game[i+3][i+3] and game[i][i] == game[i+4][i+4] and\
                game[i][i] != ' ':
                 return 1 if game[i][i] == 'X' else -1
            if (j + 5 + i) < 10:
                if game[i][j+1+i] == game[i+1][j+2+i] and game[i][j+1+i] == game[i+2][j+3+i] and\
                    game[i][j+1+i] == game[i+3][j+4+i] and game[i][j+1+i] == game[i+4][j+5+i] and\
                    game[i][j+1+i] != ' ':
                     return 1 if game[i][j+1+i] == 'X' else -1
                if game[j+1+i][i] == game[j+2+i][i+1] and game[j+1+i][i] == game[j+3+i][i+2] and\
                    game[j+1+i][i] == game[j+4+i][i+3] and game[j+1+i][i] == game[j+5+i][i+4] and\
                    game[j+1+i][i] != ' ':
                     return 1 if game[j+1+i][i] == 'X' else -1
    for i in game:
        i.reverse()
    for i in range(0,6):
        for j in range(0,5):
            if game[i][i] == game[i+1][i+1] and game[i][i] == game[i+2][i+2] and\
                game[i][i] == game[i+3][i+3] and game[i][i] == game[i+4][i+4] and\
                game[i][i] != ' ':
                 return 1 if game[i][i] == 'X' else -1
            if (j + 5 + i) < 10:
                if game[i][j+1+i] == game[i+1][j+2+i] and game[i][j+1+i] == game[i+2][j+3+i] and\
                    game[i][j+1+i] == game[i+3][j+4+i] and game[i][j+1+i] == game[i+4][j+5+i] and\
                    game[i][j+1+i] != ' ':
                     return 1 if game[i][j+1+i] == 'X' else -1
                if game[j+1+i][i] == game[j+2+i][i+1] and game[j+1+i][i] == game[j+3+i][i+2] and\
                    game[j+1+i][i] == game[j+4+i][i+3] and game[j+1+i][i] == game[j+5+i][i+4] and\
                    game[j+1+i][i] != ' ':
                     return 1 if game[j+1+i][i] == 'X' else -1
    for i in game:
        i.reverse()  
    return 0

a = [
    [' ',' ',' ',' ',' ',' ','X',' ','X','O'],
    ['X',' ','O','X',' ','X',' ','X','O',' '],
    [' ','X',' ',' ','X',' ','O',' ',' ',' '],
    [' ','O',' ','X',' ',' ',' ',' ',' ',' '],
    [' ','O','X',' ','X',' ',' ','O',' ',' '],
    [' ',' ','O',' ',' ',' ',' ','X',' ',' '],
    [' ',' ',' ',' ',' ','O',' ',' ','X',' '],
    [' ',' ',' ',' ','O','O',' ','X','X',' '],
    [' ',' ',' ','O',' ','O','X','X',' ',' '],
    [' ',' ',' ',' ',' ','X','X',' ',' ',' '],

]
print(check_game_state(a))
print(final_state_score(a))
