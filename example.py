import turtle
from drawing import *
screen = turtle.Screen()
screen.setup(width = 800, height = 800)

shapes = []

width = 50
height = width * 2

input =  turtle.textinput('Input', 'Your text goes here:')
arr = list(input.lower())

next_step = 0

for i, elem in enumerate(arr, start = 1):
  if(elem == 'a'):
    shapes.append(turtle.Turtle())
    draw_a(shapes[-1], i * width + next_step, 0, width, height)
    next_step = 20

  elif(elem == 'b'):
    shapes.append(turtle.Turtle())
    draw_b(shapes[-1], i * width + next_step, 0, width, height)
    next_step = 20

  elif(elem == 's'):
    shapes.append(turtle.Turtle())
    draw_s(shapes[-1], i  * width + next_step, 0, width, height)
    next_step = 20

screen.mainloop()
