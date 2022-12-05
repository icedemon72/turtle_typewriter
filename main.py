import turtle
from drawing import *
screen = turtle.Screen()
a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()

width = 200
height = width * 2

draw_b(a, 0, 0, width, height)

draw_a(b, width + 10, 0, width, height)

draw_s(c, 2 * width + 25, 0, width, height)


screen.mainloop()
