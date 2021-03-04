from tkinter import *
from PIL import ImageTk, Image
#import main_game


root = Tk()


#Title Definition and Title logo 
root.title('Zork-Clue')

#Map Image
map_path = r"map.jpg"
global map_image
map_image = ImageTk.PhotoImage(Image.open(map_path))
map_label = Label(root, image=map_image)

#intro_image_gui():
#Intro Image
intro_path = r"mansion.jpg"
global intro_image
intro_image = ImageTk.PhotoImage(Image.open(intro_path))
my_label = Label(root, image=intro_image)


def intro1():
    my_label.pack()
    intro_gui_label.pack()
    intro1_next_button.pack()

def intro2():
    intro2_gui_label.pack()
    map_label.pack()
    intro3_gui_label.pack()
    intro2_next_button.pack()

def intro_movement():
    intro4_gui_label.pack()
    #intro_movement_text.pack()

def intro1_delete():
    my_label.destroy()
    intro_gui_label.destroy()
    intro1_next_button.destroy()

def intro2_delete():
    intro2_gui_label.destroy()
    #map_label.destroy()
    intro3_gui_label.destroy()
    intro2_next_button.destroy()


intro1_next_button = Button(root, text="Next ->",padx=45, pady=20, command = intro1_delete)
intro2_next_button = Button(root, text="Next ->",padx=45, pady=20, command = intro2_delete)   
#intro_movement_text = Entry(root, borderwidth=8)

intro_gui_label = Label(root, text = """Welcome to Manor Mansions, the heart of this town. It's the residence of the mayor of this town. \n
Unfortunately the towns mental asylum had a security breach, one of the lunatics got out and killed the mayor's dog with a candle stick.\n
The killer has been caught but cannot be convicted until the murder weapon is found, according to interpol it's still in one of the rooms inside the mansion.\n
Help the mayor's dog get his justice by helping them find the weapon.""")

intro2_gui_label = Label(root, text = "\nYou have Entered the Mansion\n")

intro3_gui_label = Label(root, text = """\nThis is the The map of the Mansion.\n
You have Entered through the Foyer and are currently standing on the J3 tile""")

intro4_gui_label = Label(root, text = """To move up type in 'mu'\n
To move down type in 'md'\n
To move left type in 'ml'\n
To move right type in 'mr'\n""")

intro1()

intro2()

intro_movement()


#moveto = intro_movement_text.get()
"""
movement()
"""




root.mainloop()