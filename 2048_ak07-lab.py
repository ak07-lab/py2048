from numpy import *
from random import *
import os

n=int(input()or'5')
w=int(input()or'2048')
box=zeros(n*n,int)
box=box.reshape(n,n)
box[0][0]=2


def boxdisplay():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
    print(box)
    return

def up(box):
    for i in range(n-1, 0, -1):
        for j in range(n):
            if box[i-1][j] == 0 or box[i-1][j] == box[i][j]:
                box[i-1][j] = box[i-1][j] + box[i][j]
                box[i][j] = 0

    return box

def down(box):
    for i in range(n-1):
        for j in range(n):
            if box[i+1][j] == 0 or box[i+1][j] == box[i][j]:
                box[i+1][j] = box[i+1][j] + box[i][j]
                box[i][j] = 0

    return box

def left(box):
    for j in range(n-1,0,-1):
        for i in range(n):
            if box[i][j-1]==0 or box[i][j-1]==box[i][j]:
                box[i][j-1]=box[i][j-1]+box[i][j]
                box[i][j]=0

    return box


def right(box):
    for j in range(n-1):
        for i in range(n):
            if box[i][j+1] == 0 or box[i][j+1] == box[i][j]:
                box[i][j+1]=box[i][j+1]+box[i][j]
                box[i][j]=0

    return box

def assign2():
    i=randint(0,n-1)
    j=randint(0,n-1)
    if box[i][j]==0:
        box[i][j]=2
    else:
        return assign2()

def gameover(box):
    tempboard1 = copy(box)
    tempboard2 = copy(box)
    tempboard1 = up(tempboard1)
    if (tempboard1 == tempboard2).all():
        tempboard1 = down(tempboard1)
        if (tempboard1 == tempboard2).all():
            tempboard1 = left(tempboard1)
            if (tempboard1 == tempboard2).all():
                tempboard1 = right(tempboard1)
                if (tempboard1 == tempboard2).all():
                    return True

    return False

assign2()
boxdisplay()


while w not in box:
    s=input('what do u want to do(a/s/w/d)')
    if s=='w' or s=='W':
        box=up(box)
        assign2()
        boxdisplay()
    elif s=='a' or s=='A':
        box = left(box)
        assign2()
        boxdisplay()
    elif s=='s' or s=='S':
        box = down(box)
        assign2()
        boxdisplay()
    elif s=='d' or s=='D':
        box = right(box)
        assign2()
        boxdisplay()
    else:
        boxdisplay()
        print('\nINVALID INPUT!!\nTRY AGAIN WITH (W/A/S/D)\n')

    if 0 not in box:
        if gameover(box):
            print('\nGAME OVER')
            break
else:
    print('\nCONGRATULATIONS!!\n||YOU WON||')







