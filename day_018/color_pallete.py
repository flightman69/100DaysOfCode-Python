import random_color as rc
import turtle as t
from random import choice
color_pallete = rc.RandomColor.color_pallete()

ajith = t.Turtle()
screen = t.Screen()

ajith.hideturtle()
ajith.pu()
ajith.speed(0)
ajith.seth(270)
ajith.fd(400)
ajith.seth(0)
ajith.fd(200)
position = t.pos()
t.colormode(255)
for i in range(100):

    color = choice(color_pallete)
    ajith.pencolor(color)
    if i%10 == 0:
        ajith.pu()
        ajith.seth(90)
        ajith.fd(50)
        ajith.seth(180)
        ajith.fd(500)
        ajith.seth(0)
        ajith.pd()
    ajith.dot(20, color)
    ajith.pu()
    ajith.fd(50)
    ajith.pd()

screen.exitonclick()

