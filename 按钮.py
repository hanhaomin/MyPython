from tkinter import *
import random
import time

tk = Tk()

canvas = Canvas(tk, width=400, height=400, bg='grey')
canvas.pack()

mytriangle = canvas.create_polygon(10,10,10,60,50,35, fill='red', outline='yellow')

def moveit(x, y, fl, ol):
    for i in range(60):
        canvas.move(mytriangle, x, y)
        canvas.itemconfig(mytriangle, fill=fl, outline=ol)
        tk.update()
        time.sleep(1)

moveit( 5, 0, 'purple', 'red' )
moveit( 0, 5, 'white', 'purple')
moveit( -5, 0, 'orange', 'white')
moveit( 0, -5, 'blue', 'orange')

canvas.itemconfig(mytriangle, fill='red', outline='yellow')





