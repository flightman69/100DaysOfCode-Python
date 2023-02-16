import turtle
import random

ajith = turtle.Turtle()
screen = turtle.Screen()
# ajith.shape("arrow")
# ajith.color("blue","red")
# ajith.begin_fill()
# for i in range(4):
#     ajith.fd(100)
#     ajith.rt(90)
# ajith.end_fill()

# print("Printing Dashed lines")
#
# for i in range(10):
#     ajith.pd()
#     ajith.fd(10)
#     ajith.pu()
#     ajith.fd(10)


def draw_shapes(sides):
    angle = (360/sides) 

    for _ in range(sides):
        ajith.speed(5)
        ajith.fd(100)
        ajith.rt(angle)
colors = ['red','blue']
turtle.colormode(255)
for i in range(3,11):

    r  = random.randint(0, 255)
    g  = random.randint(0, 255)
    b  = random.randint(0, 255)
    ajith.pencolor((r,g,b))
    ajith.width(3)
    draw_shapes(i)
screen.exitonclick()
