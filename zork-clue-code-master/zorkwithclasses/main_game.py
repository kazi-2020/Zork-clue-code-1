from player import *
from board import *
from time import sleep
import sys
user_name=input("To play, please enter your name :- ")
  
p1=Player(user_name)

new_board = Board()

new_board.addPlayer(p1)

print("ZORK-CLUE")
intro="""Welcome to Manor Mansions, the heart of this town. It's the residence of the mayor of this town. \n
Unfortunately the towns mental asylum had a security breach, one of the lunatics got out and killed the mayor's dog with a candle stick.\n
The killer has been caught but cannot be convicted until the murder weapon is found, according to interpol it's still in one of the rooms inside the mansion.\n
Help the mayor's dog get his justice by heping them find the weapon.\n"""


for char in intro:
    sleep(0.05)
    sys.stdout.write(char)

print("You are standing in j3\n")
sleep(0.05)
print("To move up type in 'mu'\n")
sleep(0.05)
print("To move down type in 'md'\n")
sleep(0.05)
print("To move left type in 'ml'\n")
sleep(0.05)
print("To move right type in 'mr'\n")
sleep(0.05)


def movement(player):
        moveto = (input("Which way do you want to move:- "))

        if moveto == "mr" :
            new_board.moveright(player)
            new_board.current_room(player)        
        
        elif moveto == "ml" :
            new_board.moveleft(player)
            new_board.current_room(player) 
        
        elif moveto == "mu" :
            new_board.moveup(player)     
            new_board.current_room(player)    

        elif moveto == "md" :
            new_board.movedown(player)  
            new_board.current_room(player)    
        else:
            print("invalid move")
            new_board.current_room(player)

def objective_loop(player):
    print(weapon_position)
    found=0
    while found==0:
        if str(Board.board[player.x][player.y]) != str(weapon_position):
            movement(p1)
            found=0
        else:
            found=1

    print("You have found the weapon. Now the lunatic can be convicted.")

objective_loop(p1)