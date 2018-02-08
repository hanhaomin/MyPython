from tkinter import *
import time

class MyTriangle:
    def __init__(self, tk, canvas, fill, outline):
        self.tk = tk
        self.canvas = canvas
        self.fill = fill
        self.outline = outline

    def create(self):
        self.id = self.canvas.create_polygon(10,10,10,60,50,35, fill=self.fill, outline=self.outline)

    def moveRight(self, step):
        for x in range(step):
            self.canvas.move(self.id, 5, 0)
            self.canvas.itemconfig(self.id, fill='purple', outline='red')
            self.tk.update()
            time.sleep(0.05)

    def moveDown(self, step):
         for x in range(step):
            self.canvas.move(self.id, 0, 5)
            self.canvas.itemconfig(self.id, fill='white', outline='purple')
            self.tk.update()
            time.sleep(0.05)

    def moveLeft(self, step):
        for x in range(step):
            self.canvas.move(self.id, -5, 0)
            self.canvas.itemconfig(self.id, fill='orange', outline='white')
            self.tk.update()
            time.sleep(0.05)

    def moveUp(self, step):
        for x in range(step):
            self.canvas.move(self.id, 0, -5)
            self.canvas.itemconfig(self.id, fill='blue', outline='orange')
            self.tk.update()
            time.sleep(0.05)