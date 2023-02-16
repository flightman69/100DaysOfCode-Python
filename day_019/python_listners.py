import turtle

ajith = turtle.Turtle()
screen = turtle.Screen()

ajith.speed(0)
def quit():
    turtle.bye()


def move_up():
    ajith.setheading(90)
    ajith.fd(10)

def move_rt():
    ajith.setheading(0)
    ajith.fd(10)

def move_dn():
    ajith.setheading(270)
    ajith.fd(10)

def move_lt():
    ajith.setheading(180)
    ajith.fd(10)


screen.listen()
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_dn)
screen.onkey(key="Right", fun=move_rt)
screen.onkey(key="Left", fun=move_lt)

screen.onkey(key="q", fun=quit)
screen.exitonclick()
