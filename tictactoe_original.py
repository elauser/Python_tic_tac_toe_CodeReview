from random import randrange
result = False
board=[[1,2,3],[4,'X',6],[7,8,9]]
#
#board initialization always first move of computer is in the middle

def DisplayBoard(board):
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
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
def EnterMove(board):
    entredMove=int((input("Enter your move: ")))
    while not any(entredMove in i for i in board):
            print ("this value is wrong")
            entredMove=int((input("Enter your move: ")))
    for i in range(3):
        for j in range(3):
            if int(entredMove)==board[i][j]:
                board[i][j]= 'O'
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    freeFields=[]
    s=0
    global result
    for i in range(3):
        for j in range(3):
            if type(board[i][j])== int:
                freeFields.append((i,j))
                s+=1
    if s==0 and result==False:
        result = True
        print ("it is a DRAW")    
                    

# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
# and test if list is empty that means it is a draw

def VictoryFor(board, sign):
    global result
    xxx=0
    xxxx=0
    for i in range(3):
        x=0
        for j in range(3):
            if board[i][j]==sign:
                x+=1
                if x==3:
                    print(sign,' is won the game')
                    result=True
        if result == True:
            break
        xx=0
        for j in range(3):
            if board[j][i]==sign:
                xx+=1
                if xx==3:
                    print(sign,' is won the game')
                    result=True
        if result == True:
            break
        for j in range(3):
            if i==j and board[i][j]==sign:
                xxx+=1
                if xxx==3:
                    print(sign,' is won the game')
                    result=True
        if result ==True:
            break
        for j in range(3):
            if i+j==2 and board[i][j]==sign:
                xxxx+=1
                if xxxx==3:
                    print(sign,' is won the game')
                    result=True
        if result ==True:
            break
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game 
#

def DrawMove(board):
    entredMove=randrange(8)+1
    while not any(entredMove in i for i in board):
        entredMove=randrange(9)+1
    for i in range(3):
        for j in range(3):
            if int(entredMove)==board[i][j]:
                print('computer move in ',entredMove)
                board[i][j]= 'X'
#
# the function draws the computer's move and updates the board
#
DisplayBoard(board)
while result == False:
    EnterMove(board)
    DisplayBoard(board)
    VictoryFor(board, 'O')
    if result == False:
        DrawMove(board)
        VictoryFor(board, 'X')
        DisplayBoard(board)
        MakeListOfFreeFields(board)