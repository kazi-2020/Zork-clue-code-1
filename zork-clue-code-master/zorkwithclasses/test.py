from player import Player
from board import Board

#testing creating new players
p_Anush=Player("Anush")
p_som = Player("som")

#creating an instance of the board
new_board = Board()

#adding player to the board
new_board.addPlayer(p_Anush)
new_board.addPlayer(p_som)

new_board.printAllPlayers()
"""
#Testing a door in the way

#Testing move right for 1 player p_Anush
print(p_Anush.name)
new_board.moveright(p_Anush)

#testing move right for two players (p_som as well)
print(p_som.name)
new_board.moveright(p_som) 

#Testing move left for 1 player p_Anush
print(p_Anush.name)
new_board.moveleft(p_Anush)

#testing move left for two players (p_som as well)
print(p_som.name)
new_board.moveleft(p_som) 

#Testing move up for 1 player p_Anush
print(p_Anush.name)
new_board.moveup(p_Anush)

#testing move up for two players (p_som as well)
print(p_som.name)
new_board.moveup(p_som) 

#Testing move down for 1 player p_Anush
print(p_Anush.name)
new_board.movedown(p_Anush)

#testing move down for two players (p_som as well)
print(p_som.name)
new_board.movedown(p_som) 

#Testing move down second time for 1 player p_Anush
print(p_Anush.name)
new_board.movedown(p_Anush)

#testing move down for two players second time (p_som as well)
print(p_som.name)
new_board.movedown(p_som) 
"""

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


for turn in range(1,3000):
    movement(p_Anush)

