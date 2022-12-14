from turtle import Turtle, Screen
import random


def color():
    r = random.random()
    g = random.random()
    b = random.random()

    tim.color((r, g, b))


tim = Turtle()
tim.shape('turtle')
tim.speed('fastest')
tim.pensize(5)

for _ in range(72):
    tim.circle(200)
    tim.right(5)
    color()


screen = Screen()
screen.exitonclick()
