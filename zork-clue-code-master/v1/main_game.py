from board import *
from movement import *
from restrictions import *
from whichroom import *
import whichroom
import sys
from time import sleep
import random

print("ZORK-CLUE")
intro="""Welcome to Manor Mansions, the heart of this town. It's the residence of the mayor of this town. \n
Unfortunately the towns mental asylum had a security breach, one of the lunatics got out and killed the mayor's dog with a candle stick.\n
The killer has been caught but cannot be convicted until the murder weapon is found, according to interpol it's still in one of the rooms inside the mansion.\n
Help the mayor's dog get his justice by heping them find the weapon.\n"""

for char in intro:
    sys.stdout.write(char)
    sleep(0.05)
    

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

"""
 for i in range (1,1500):88
    movement()
"""    
    
print(weapon_position)
found=0
while found==0:
    if str(pos) != str(weapon_position):
        movement()
        found=0
    else:
        found=1

print("You have found the weapon. Now the lunatic can be convicted.")


