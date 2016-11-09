import turtle
from math import sin, pi
def heart(size, shape):
    turtle.pensize(10)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    turtle.right(shape)
    turtle.forward(size)
    turtle.circle(radius, 180 + shape)
    turtle.right(180)
    turtle.circle(radius, 180 + shape)
    turtle.forward(size)
    turtle.left(180 - shape)