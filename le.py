import turtle

t = turtle.Pen()



def mycircle(red, green, blue):
    t.color(red, green, blue)
    t.begin_fill
    t.circle(50)
    t.end_fill

# t.up()
# t.backward(250)
# t.down()

for x in range(6):
    mycircle(0,1,0)
    t.up()
    t.forward(100)
    t.down()
    if x % 2 == 1:
        t.up()
        t.backward(200)
        t.right(90)
        t.forward(100)
        t.left(90)
        t.down()


#mycircle(0, 1, 0)
#mycircle(0, 0.5, 0)

#t.color(0,0,0)
#t.begin_fill()
#t.circle(50)
#t.end_fill

