def extractPlayer(board,player):
    res = list()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 'X'):
                res.append([i,j])
    return res

def setMove(board,idx,player):
    board[idx[0]][idx[1]] = player

def printBoard(board):
    for i in board:
        print("--"*(len(i)+1))
        print("|",end="")
        for j in i:
            print(str(j)+"|",end="")
        print()
    print("--"*(len(i)+1))


def checkForWin(board,player):
    idx = extractPlayer(board,player)
    diagonal_flag = column_flag = False
    idx_map = dict()
    for i in idx:
        if 'r'+str(i[0]) not in idx_map:
            idx_map['r'+str(i[0])] = 1
        else:
            idx_map['r'+str(i[0])] += 1
        if 'c'+str(i[1]) not in idx_map:
           idx_map['c'+str(i[1])] = 1
        else:
           idx_map['c'+str(i[1])] += 1
        if abs(i[0] - i[1]) == 0:
            if 'd1' in idx_map:
                idx_map['d1'] +=1
            else:
                idx_map['d1'] = 1
        if i[0] + i[1] == 2:
            if 'd2' in idx_map:
                idx_map['d2'] += 1
            else:
                idx_map['d2'] = 1
    for i in idx_map.values():
           if i==3:
                return True
    return False

def switchPlayer(player):
    return 'O' if player=='X' else 'X'

def validateInput(board,row,col):
    if col < 1 or row < 1 or col > 3 or row > 3:
        return 1
    if not board[row-1][col-1]==" ":
        return 1
    return 0
def playGame():
    board = list()
    for i in range(3):
        board.append([" "]*3)
    printBoard(board)
    player = 'X'
    playerCount = 1
    print("Eg index selection: 1 1 corresponds to the top left square")
    while(not checkForWin(board,player)):
        row,col = input(f"Player {player}'s move\n : ").split()
        row = int(row)
        col = int(col)
        while(validateInput(board,row,col)):
            print("Invalid move.Enter again.")
            row,col = input(f"Player {player}'s move\n : ").split()
            row = int(row)
            col = int(col)
        setMove(board,[row-1,col-1],player)
        printBoard(board)
        if(checkForWin(board,player)):
            print(f"{player} Wins")
            return 1
        player = switchPlayer(player)
    print("Draw")
    return -1
while(True):
    print("======================\n+       MENU         +\n======================")
    choice =int(input("Select a choice\n1).Play\n2).Exit\n"))
    if(choice==2):
        break
    elif(choice == 1):
        playGame()
    else:
        print("Invalid option. Try again") 
