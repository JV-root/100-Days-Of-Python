# The challenge is to draw an square using the turtle library.
from turtle import *


def square(turtle):
    for k in range(0, 4):
        turtle.forward(100)
        turtle.left(90)


square(Turtle())