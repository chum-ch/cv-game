import tkinter as tk
import random
# creating tkinter window 
root = tk.Tk() 
root.geometry("450x450")
canvas = tk.Canvas(root)
root.title("Game VC") 
# Creating Menu 
menu_file = tk.Menu(root) 
# Adding File Menu and sub file 
file = tk.Menu(menu_file, tearoff = 0)
menu_file.add_cascade(label ="File", menu = file)
# Adding "New level" inside of the file
file.add_command(label ="New level")
# Adding "Exit" inside of the file
file.add_command(label ="Exit", command = root.destroy) 


# CONSTANTS
SIZE = 40
index_of_one = 0
index_of_two = 0
# 0 gird
# 1 is firewall
# 2 person
# 3 the box
boradgame = [
    [1,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0],
    [2,0,0,3,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,0]

]
def arrayToDrawing():
    global boradgame, index_of_one, index_of_two
    for index1 in range (len(boradgame)):
        for index2 in range(len(boradgame[0])):
            x1=SIZE * index2
            y1=SIZE * index1
            x2=SIZE + x1
            y2=SIZE + y1
            # draw a line with white and black squares using the global array
            if boradgame[index1][index2] == 1:
                color="black"
            elif boradgame[index1][index2] == 2:
                color = "purple"
                index_of_two = index2
                index_of_one = index1
            else:
                color="white"
            canvas.create_rectangle(x1,y1,x2,y2,fill=color, outline = "#fff")
def moveRight(event):
    global boradgame, index_of_one, index_of_two
    if index_of_two < len(boradgame[0]) - 1:
        index_of_two += 1
    boradgame[index_of_one][index_of_two] = 2
    boradgame[index_of_one][index_of_two-1] = 0
    arrayToDrawing()


def moveLeft(event):
    global boradgame, index_of_one, index_of_two
    if index_of_two > 0:
        index_of_two -= 1
    boradgame[index_of_one][index_of_two] = 2
    boradgame[index_of_one][index_of_two+1] = 0
    arrayToDrawing()


def moveUp(event):
    global boradgame, index_of_one, index_of_two
    if index_of_one > 0:
        index_of_one -= 1
    boradgame[index_of_one][index_of_two] = 2
    boradgame[index_of_one+1][index_of_two] = 0
    arrayToDrawing()


def moveDown(event):
    global boradgame, index_of_one, index_of_two
    if index_of_one < len(boradgame) - 1:
        index_of_one += 1
    boradgame[index_of_one][index_of_two] = 2
    boradgame[index_of_one-1][index_of_two] = 0
    arrayToDrawing()

arrayToDrawing()
root.bind("<Left>", moveLeft)
root.bind("<Right>", moveRight)
root.bind("<Up>", moveUp)
root.bind("<Down>", moveDown)
canvas.pack(expand=True, fill='both')
# display Menu 
root.config(menu = menu_file) 
root.mainloop()