import turtle

t = turtle.Pen()

def draw_star(size, points):
    for x in range(points):
        angle = 360 / points
        t.forward(size)
        t.left( 180 - angle )
        t.forward(size)
        t.right( 180 - (angle * 2) )


for x in range(10):
    draw_star(50 + 5 * x, 5 + x)
