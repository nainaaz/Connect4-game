#Connect4 game

def make_empty_board(nrows,ncols):
    return ["."*ncols] * nrows

def print_board(lst):
    a=0
    for chance in lst:
        i=0
        b=0
        while b<(len(chance))-1:
            if chance[i]==".":
                print('   '+'|',end='')
            elif chance[i]=="X":
                print(' X '+'|',end='')
            elif chance[i]=="O":
                print(' O '+'|',end='')
            b+=1
            i+=1
        if chance[-1]==".":
            print('   ')
        elif chance[-1]=="X":
            print(' X ')
        elif chance[-1]=="O":
            print(' O ')

        if a<(len(lst))-1:
            print('---+'*(len(chance)-1)+'---')
        a+=1

def verify_board(board):
    a=0
    b=0
    for i in board:
        for j in i:
            if j=="X":
                b+=1
            elif j=="O":
                a+=1
    if b-a>=2 or a-b>=2:
        return False
    
    for s in range(len(board)-1,-1,-1):
        for t in range(len(board[s])):
            if board[s][t]=="X":
                if s!=len(board)-1:
                    if board[s+1][t]==".":
                        return False             
            elif board[s][t]=="O":
                if s!=len(board)-1:
                    if board[s+1][t]==".":
                        return False
    return True

def verify_move(board, col):
    if col<0 or col>=len(board[0]):
        return False
    if board[0][col] == ".":
        return True
    else:
        return False

def update_board(board,int,disc):
    for i in  range((len(board))-1,-1,-1):
        if board[i][int]==".":
            lst=list(board[i])
            lst[int]=disc
            str=""
            board[i]=str.join(lst)
            break
    return board

def has_won(board, column):
    for i in range(len(board)):
        if board[i][column]!=".":
            row_top=i
            leftcol=1
            rightcol=1
            row_score=1
            ll2ur=1
            ul2lr=1
            break
    
    for j in range(row_top+1, len(board)):
        if board[j][column] == board[i][column]:
            row_score+=1
        else:
            break
    
    for s in range(column-1,-1,-1):
        if board[row_top][s]==board[i][column]:
            leftcol+=1
        else:
            break

    if leftcol>=4 or row_score>=4:
        return True

    for t in range(column+1,len(board[0])):
        if board[row_top][t]==board[i][column]:
            rightcol+=1
        else:
            break

    if rightcol>=4 or (leftcol+rightcol)-1>=4:
        return True

    row=row_top+1
    col=column-1
    while row<len(board) and col>=0 and board[row][col]==board[i][column]:
        ll2ur+=1
        row+=1
        col-=1

    row=row_top-1
    col=column+1
    while row>=0 and col<len(board[0]) and board[row][col]==board[i][column]:
        ll2ur+=1
        row-=1
        col+=1

    row=row_top-1
    col=column-1
    while row>=0 and col>=0 and board[row][col]==board[i][column]:
        ul2lr+=1
        row-=1
        col-=1

    row=row_top+1
    col=column+1
    while row<len(board) and col<len(board[0]) and board[row][col]==board[i][column]:
        ul2lr+=1
        row+=1
        col+=1

    if ul2lr>=4 or ll2ur>=4:
        return True
    else:
        return False
