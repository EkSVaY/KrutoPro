import turtle
def triangle(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor("white")
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.left(90)
    turtle.fd(a)
    turtle.right(135)
    turtle.fd((2*a**2)**0.5)
    turtle.left(225)
    turtle.fd(a)
    turtle.end_fill()
    turtle.up()
    turtle.home()

def star(x, y, a, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.pensize(2)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.fd(a)
        turtle.right(144)
    turtle.end_fill()

def circle(x, y, r, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()
    turtle.up()

def rectangle(x, y, a, b, color):
    turtle.color(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.end_fill()

def square(x, y, a, color):
    turtle.color(color)
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()



def paral(x, y, a, b, v, color):
    turtle.setposition(x, y)
    turtle.fillcolor(color)
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.begin_fill()
    if v == 1:
        for i in range(2):
            turtle.forward(a)
            turtle.left(130)
            turtle.forward(b)
            turtle.left(50)
    elif v == 2:
        for i in range(2):
            turtle.forward(a)
            turtle.left(45)
            turtle.forward(b)
            turtle.left(135)
    turtle.end_fill()



def trap(x, y, a, b, c, r1, r2, color):
    turtle.setposition(x, y)
    turtle.fillcolor(color)
    turtle.pencolor('white')
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(130)
    turtle.forward(b)
    turtle.left(50)
    turtle.forward(c)
    turtle.left(50)
    turtle.forward(b)
    turtle.left(130)
    turtle.end_fill()
