import turtle

t = turtle.Pen()

t.color('black','yellow')

t.begin_fill()
for x in range(8):
    t.forward(50)
    t.right(45)
t.end_fill()
