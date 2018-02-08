from tkinter import *
import random
import time
import MyTriangle

tk = Tk()

canvas = Canvas(tk, width=400, height=400, bg='grey')
canvas.pack()

t = MyTriangle.MyTriangle(tk, canvas, 'red', 'yellow')
t.create()

t1 = MyTriangle.MyTriangle(tk, canvas, 'red', 'yellow')
t1.create()

t.moveRight(60)
t1.moveDown(60)

t.moveDown(60)
t1.moveRight(60)

t.moveLeft(60)
t1.moveUp(60)

t.moveUp(60)
t1.moveLeft(60)

tk.mainloop()





