import turtle

ajith = turtle.Turtle()
screen = turtle.Screen()

ajith.pensize(4)

def fd():
    ajith.fd(10)

def bk():
    ajith.bk(10)

def cw():
    ajith.right(10)
def ccw():
    ajith.left(10)

def quit():
    turtle.bye()

def clear():
    turtle.resetscreen()
    ajith.pensize(4)


screen.listen()
screen.onkey(key="w", fun=fd)
screen.onkey(key="s", fun=bk)
screen.onkey(key="d", fun=cw)
screen.onkey(key="a", fun=ccw)
screen.onkey(key="q", fun=quit)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
