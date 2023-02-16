import turtle, random

ajith = turtle.Turtle()
screen = turtle.Screen()

turtle.setup(50, 50)
turtle.colormode(255)
angles = [0, 90, 180, 270]
screen.bgcolor("black")
for _ in range(10000):
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    ajith.pencolor((r, g, b))
    ajith.width(10)
    ajith.speed(0)
    ajith.fd(30)
        
    turn = random.choice(angles)
    ajith.setheading(turn)

screen.exitonclick()
