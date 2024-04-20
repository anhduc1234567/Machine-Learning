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

def print_game(game):
    for i in range(0,10):
        for j in range(0,10):
            print(f'| {game[i][j]} |',end='')
        print()

def current_player(game):
    x = 0
    o = 0
    for i in range(0,10):
        for j in range(0,10):
            if game[i][j] == 'X':
                x += 1
            elif game[i][j] == 'O':
                o += 1
    if x == o:
        return 'X'
    else:
        return 'O'

def create_board(n):
    board = []
    for i in range(0,n):
        board.append([' '] * n)
    return board

def copy_move(a,b,game,player):
    game_new = create_board(10)
    for i in range(0,10):
        for j in range(0,10):
            game_new[i][j] = game[i][j]
    
    game_new[a][b] = player
    return game_new

def valid_move(game):
    player = current_player(game)
    result = []
    for i in range(0,10):
        for j in range(0,10):
            if game[i][j] == ' ':
                game_new = copy_move(i,j,game,player)
                # game_new[i][j] = player
                result.append(game_new)
    return result

def final_state_score(game):
    for i in range(0,3):
        if game[i][0] == game[i][1] and game[i][0] == game[i][2] and game[i][0] != ' ':
            return 1 if game[i][0] == 'X' else  -1
    for i in range(0,3):
        if game[0][i] == game[1][i] and game[0][i] == game[2][i] and game[0][i] != ' ':
            return 1 if game[0][i] == 'X' else -1
    if game[0][0] == game[1][1] and game[0][0] == game[2][2] and game[0][0] != ' ':
        return 1 if game[0][0] == 'X' else -1
    if game[0][2] == game[1][1] and game[0][2] == game[2][0] and game[0][2] != ' ':
        return 1 if game[0][2] == 'X' else -1
    return 0

def state_value(game,time):
    if check_game_state(game):
        return final_state_score(game)
    if time == 11:
        return 1
    move = valid_move(game)
    NO_VALUE = -100
    player = current_player(game)
    result = NO_VALUE
    for m in move:
        score = state_value(m,time+1)
        if player == 'X':
            if result == NO_VALUE or result < score:
                result = score
        if player == 'O':
            if result == NO_VALUE or result > score:
                result = score
    return result

def best_move(game):
    move = valid_move(game)
    print(len(move))
    player = current_player(game)
    NO_VALUE = -100
    bestscore = NO_VALUE 
    bestmoves = create_board(10)
    for m in move:
        score = state_value(m,10)
        if player == 'X':
            if bestscore == NO_VALUE or bestscore < score:
                bestscore = score
                bestmoves = m
        if player == 'O':
            if bestscore == NO_VALUE or bestscore > score:
                bestscore = score
                bestmoves = m
    for i in range(0,10):
        for j in range(0,10):
            if bestmoves[i][j] != game[i][j]:
                return (i,j)
    
    return (-1,-1)

def check_cordinate(x,y,game):
    if x < 0 or x > 9 or y < 0 or y > 9:
        return False
    if game[x][y] == ' ':
        return True
    else:
        return False

    return True         

game = create_board(10)

current_playerr = 'X'
human = 'X'
while True:
    if human == current_playerr:
        print('Nhập tọa độ: ')
        a = input().split()
        x = int(a[0])
        y = int(a[1])
        if check_cordinate(x,y,game) == True:
            print(f'Nguoi chon : {x} - {y}')
        else:
            print('Loi toa do ')
    else:
        robot = best_move(game)
        x = robot[0]
        y = robot[1]
        print(f'máy chọn: {x} - {y}')
    
    game = copy_move(x,y,game,current_playerr)
    print_game(game)
    if current_playerr == 'X':
        current_playerr = 'O'
    else:
        current_playerr = 'X'
    
    if check_game_state(game) == True:
        s = final_state_score(game)
        if s == 1 and human == 'X':
            print('Human win:')
        elif s == 1 and human =='O':
            print('Human lose')
        elif s == -1 and human == 'O':
            print('Hum win ')
        elif s == -1 and human == 'X':
            print('Human lose ')
        else:
            print('Draw')
        break
