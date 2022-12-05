import turtle
from drawing import *
screen = turtle.Screen()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()

width = 50
height = width * 2

draw_b(a, 0, 0, width, height)

draw_a(a, width + 10, 0, width, height)

draw_s(a, 2 * width + 25, 0, width, height)

screen.mainloop()
