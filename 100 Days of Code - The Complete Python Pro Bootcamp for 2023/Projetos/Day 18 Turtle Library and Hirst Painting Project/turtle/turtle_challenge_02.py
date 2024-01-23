# The challenge is to draw an dashed line using the turtle library.
from turtle import *


def dashed_line(turtle):
    for k in range(0, 10):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

dashed_line(Turtle())