from board import *

present_room=" this room"
def current_room(position):
    
    global present_room
    
    if position in storage:
        print("Player is in storage.")
        present_room="storage"
        
    elif position in study:
        print("Player is in study.")
        present_room="study"
    
    elif position in bathroom:
        print("Player is in bathroom.")
        present_room="bathroom"
    elif position in lib:
        print("Player is in library.")
        present_room="lib"
    
    elif position in gallery:
        print("Player is in gallery.")
        present_room="gallery"
    
    elif position in bed1:
        print("Player is in bedroom 1.")
        present_room="bed1"
    
    elif position in foyer:
        print("Player is in foyer.")
        present_room="foyer"
    
    elif position in bed2:
        print("Player is in bedroom 2.")
        present_room="bed2"
    elif position in kitchen:
        print("Player is in kitchen.")
        present_room="kitchen"
    else:
        print("Player is in hallway")
        present_room="hallway"
        


