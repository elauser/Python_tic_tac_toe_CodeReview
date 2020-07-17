from random import randrange
board=[[1,2,3],[4,'X',6],[7,8,9]]


def play_game():
    display_board(board)
    won = False
    draw = False
    while won == False and draw == False:
        enter_move_player(board)
        display_board(board)
        won = has_won(board, 'O')
        if won == False:
            enter_move_computer(board)
            won = has_won(board, 'X')
            display_board(board)
            draw = is_draw(board)


def display_board(board):
    for j in range(4):
        for i in range(4):
            print("+",end='')
            if i==3:
                break
            for i in range(7):
                print("-",end='')
        if j==3:
            break
        print()
        for d in range (3):
            for r in range(4):
                print("|",end='')
                if r==3:
                    break
                for i in range(7):
                    if d==1 and i==3:
                        print(board[j][r],end='')
                    else:
                        print(" ",end='')
            print()
    print()


def enter_move_player(board):
    enteredMove=int((input("Enter your move: ")))
    while not any(enteredMove in i for i in board):
            print ("this value is wrong")
            enteredMove=int((input("Enter your move: ")))
    for i in range(3):
        for j in range(3):
            if int(enteredMove)==board[i][j]:
                board[i][j]= 'O'


def is_draw(board):
    freeFields=[]
    s=0
    for i in range(3):
        for j in range(3):
            if type(board[i][j])== int:
                freeFields.append((i,j))
                s+=1
    if s==0 and result==False:
        print ("it is a DRAW")  
        return True
    return False
                    

def has_won(board, player):
    if (
        has_won_vertically(board, player) or 
        has_won_horizontally(board, player) or 
        has_won_diagonal_1(board, player) or 
        has_won_diagonal_2(board, player)):
        return True
    return False


def has_won_vertically(board, player):
    for row in range(3):
        player_count = 0
        for column in range(3):
            if board[row][column] == player:
                player_count += 1
        if player_count == 3:
            return True
    return False

def has_won_horizontally(board, player):
    for column in range(3):
        player_count = 0
        for row in range(3):
            if board[row][column] == player:
                player_count += 1
        if player_count == 3:
            return True
    return False

def has_won_diagonal_1(board, player):
    player_count = 0
    for row in range(3):
        for column in range(3):
            if row == column and board[row][column] != player:
                return False
    return True

def has_won_diagonal_2(board, player):
    player_count = 0
    for row in range(3):
        for column in range(3):
            if row+column == 2 and board[row][column] != player:
                return False
    return True

def enter_move_computer(board):
    enteredMove = randrange(8)+1
    while not any(enteredMove in i for i in board):
        enteredMove=randrange(9)+1
    for i in range(3):
        for j in range(3):
            if int(enteredMove)==board[i][j]:
                print('computer move in ',enteredMove)
                board[i][j]= 'X'

if __name__ == "__main__" :
    play_game()