import random


def board(arr):

    for i in range(3):
        for j in range(3):
            print(arr[i][j],end=" ")
        print()
    print()

def score(arr):

    for i in range (3):
        if(arr[i][0]==arr[i][1] and arr[i][1]==arr[i][2]):
            if(arr[i][0]=='X'):
                return 10
            elif(arr[i][0]=='O'):
                return -10

    for j in range (3):
        if(arr[0][j]==arr[1][j] and arr[1][j]==arr[2][j]):
            if(arr[0][j]=='X'):
                return 10
            elif(arr[0][j]=='O'):
                return -10

    if((arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2]) or (arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0])):
        if(arr[1][1]=='X'):
            return 10
        elif(arr[1][1]=='O'):
            return -10

    return 0

def empty(arr):
    for i in range (3):
        for j in range (3):
            if(arr[i][j]==' '):
                return True
    return False

def minmax(arr,dep,maxim):
    points=score(arr)
    if(points==10):
        return points-dep
    elif(points==-10):
        return points+dep
    elif(not empty(arr)):
        return 0
    
    if(maxim):
        best=-1000
        for i in range(3):
            for j in range (3):
                if(arr[i][j]==' '):
                    arr[i][j]='X'
                    best=max(best,minmax(arr,dep+1,not maxim))
                    arr[i][j]=' '
        return best
    else:
        best=1000
        for i in range(3):
            for j in range (3):
                if(arr[i][j]==' '):
                    arr[i][j]='O'
                    best=min(best,minmax(arr,dep+1,not maxim))
                    arr[i][j]=' '
        return best

def bestmove(arr):
    best=-1000
    move=[-1,-1]
    for i in range(3):
        for j in range(3):
            if(arr[i][j]==' '):
                arr[i][j]='X'
                newscore=minmax(arr,0,False)
                arr[i][j]=' '
                if(newscore>best):
                    best=newscore
                    move=[i,j]
    
    arr[move[0]][move[1]]='X'
    return arr

def userinput(arr):
    print("Enter your move")
    inp=list(map(int,input().split()))
    arr[inp[0]][inp[1]]= 'O'
    return arr

def Toss():
    play= random.randint(1,2)
    return play

def tictactoe():
    game=[]
    for i in range(3):
        game.append([' ',' ',' '])

    emp=True
    i=Toss()

    if(i&1):
        print("You won the toss. Play!")
    else:
        print("Sorry! AI plays first")

    points=0
    while(emp and points==0):
        if(i&1):
            game=userinput(game)
        else:
            game=bestmove(game)
        
        points=score(game)
        board(game)
        i+=1
        emp=empty(game)

    if(points==10):
        print("AI wins")
    elif (points==-10):
        print("You win")
    else:
        print("Draw")
    
tictactoe()