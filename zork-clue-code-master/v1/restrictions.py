from board import *
from whichroom import *
def moveright():
     global y
     global pos
     if y>=0 and y<len(board)-1:
          if board[x][y+1]==" ":
               y=y+2
               pos=board[x][y]
               print("Player is standing in ", pos,".")
               #print(y)
          elif  board[x][y+1]=="d":
               choice=input("Do you chose to open the door?y or n :-")    
               if choice=="y":
                    y=y+2
                    pos= board[x][y]
                    print("Player is standing in ", pos,".")
               elif choice=="n":
                    print("Player is standing in the same place ", pos,".")
               else:
                    print("Invalid input.")
     
          else:
               print("There is a wall")
     else:
          print("Player is standing at boundary.") 
     
     
def moveleft():
     global pos
     global y
     if  y<=len(board)-1 and y>0:
          if board[x][y-1]==" ":
               y=y-2
               pos=board[x][y]
               print("Player is standing in ", pos,".")
               #print(y)
     
          elif board[x][y-1]=="d":
          
               choice=input("Do you chose to open the door?y or n :-")
               if choice=="y":
                    y=y-2
                    pos= board[x][y]
                    print("Player is standing in ", pos,".")
               elif choice=="n":
                    print("Player is standing in the same place ", pos,".")
               else:
                    print("Invalid input.")
     
          else:
               print("There is a wall.")
     else:
          print("Player is standing at boundary.")
     

def moveup():
     global x
     global pos
     if  x<=len(board)-1 and x>0:    
          if board[x-1][y]==" ":
               x=x-2
               pos=board[x][y]
               print("Player is standing in ", pos,".")
               #print(x)
          
          elif board[x-1][y]=="d":
          
               choice=input("Do you chose to open the door?y or n :-")
               if choice=="y":
                    x=x-2
                    pos= board[x][y]
                    print("Player is standing in ", pos,".")
               elif choice=="n":
                    print("Player is standing in the same place ", pos,".")
               else:
                    print("Invalid input.")
          
          else:
               print("There is a wall.")
     
     else:
          print("Player is standing at boundary.") 
     

def movedown():
     global x
     global pos
     if x>=0 and x<len(board)-1:    
          if board[x+1][y]==" ":
               x=x+2
               pos=board[x][y]
               print("Player is standing in ", pos,".")
               #print(x)
          elif board[x+1][y]=="d":
               choice=input("Do you chose to open the door?y or n :-")
               if choice=="y":
                    x=x+2
                    pos= board[x][y]
                    print("Player is standing in ", pos,".")
               
               elif choice=="n":
                    
                    print("Player is standing in the same place ", pos,".")
               
               else:
                    print("Invalid input.")
          
          else:
               print("There is a wall.")
          
     else:
          print("Player is standing at boundary.")  

     

