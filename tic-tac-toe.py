#make use of OOP
from tkinter import *
import random

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X","O"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text = player + "turn", font=("roman",40))
label.pack(side = "top")

resetbutton = Button(text = "restart", font =('consolas',20),command = new_game)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in rnage(3):
        buttons[row][column] = Button(frame, text = "",fo)
window.mainloop()
