from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snek gem')

segment_1 = Turtle('square')
segment_1.color('white')

screen.exitonclick()

