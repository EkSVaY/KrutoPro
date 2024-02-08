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

