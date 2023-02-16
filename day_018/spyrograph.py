import turtle as t
import random
from random_color import RandomColor
ajith = t.Turtle()
screen = t.Screen()
ajith.width(3)
ajith.speed(0)
t.colormode(255)
screen.bgcolor("black")
ajith.pencolor("white")
t.colormode(255)
def draw_spyrograph(size):
    for _ in range(360//size):

        color = RandomColor.rand_color()
        ajith.pencolor(color)
        ajith.circle(200)
        ajith.rt(size)

draw_spyrograph(5)
screen.exitonclick()
