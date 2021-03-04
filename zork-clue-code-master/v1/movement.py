from restrictions import *
from whichroom import *
from board import *
import restrictions


def movement():
    moveto = (input("Which way do you want to move:- "))
    global pos
    global x
    global y
    if moveto == "mr" :
            
        moveright()
        current_room(restrictions.pos)      
    elif moveto == "ml" :
            
        moveleft()
        current_room(restrictions.pos) 
    elif moveto == "mu" :
       moveup()     
       current_room(restrictions.pos)     
    
    elif moveto == "md" :
        movedown()  
        current_room(restrictions.pos)    
    else:
        print("invalid move")    

#test loop

#movement()
