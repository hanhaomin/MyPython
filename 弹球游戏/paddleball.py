from tkinter import *
import random
import time
from ball import *

tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

allBall = []

paddle = Paddle(canvas, 'blue')

randColor = ['red', 'blue', 'yellow', 'black', 'purple']

for x in range(1):
    random.shuffle(randColor)
    ball = Ball(canvas, randColor[0], 100, 20*x)
    allBall.append( ball )

while 1:
    for x in range(1):
        allBall[x].draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

