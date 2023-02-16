from turtle import Screen, Turtle, pd, textinput
from random import randint

def print_race_track():
    drawer = Turtle()
    drawer.hideturtle()
    drawer.pu()
    drawer.goto(x=-320, y=-150)
    drawer.pensize(4)
    drawer.pd()
    drawer.fd(700)

    drawer.pu()
    drawer.goto(x=-320, y=150)
    drawer.pd()
    drawer.fd(700)

    drawer.pu()
    drawer.goto(x=250, y=-140)
    drawer.setheading(90)
    drawer.pd()
    drawer.color("red")
    drawer.fd(280)


print_race_track()
is_race_on = False
screen = Screen()
screen.setup(width=400, height=400)
user_bet = screen.textinput(title="Make Bet", prompt="Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =[]
y_pos = [-120, -70, -20, 30, 80, 130]

for turtle_index in range(6):
    ajith = Turtle(shape="turtle")
    ajith.pu()
    ajith.color(colors[turtle_index])

    ajith.goto(x=-300, y=y_pos[turtle_index])
    all_turtles.append(ajith)
print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for aamais in all_turtles:
        if aamais.xcor() > 230:
            is_race_on = False
            winning_color = aamais.pencolor()

            if winning_color == user_bet:
                print(f"You've won! {winning_color} aamai won the race" )
            else:
                print(f"Sorry you've lost {winning_color} was the winner")
        rand_distance = randint(0, 10)
        aamais.fd(rand_distance)


screen.exitonclick()
