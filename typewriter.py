import turtle
from drawing import *
screen = turtle.Screen()
screen.setup(width = 800, height = 800)

shapes = []

next_step = 0

def remove_letter():
  global shapes
  if(len(shapes)):
    shapes[-1].clear()
    del shapes[-1]

def type_letter(letter):
  width = 50
  height = width * 2
  global shapes
  global next_step

  shapes.append(turtle.Turtle())
  shapes[-1].speed(0)
  if(letter == 'a'):
    draw_a(shapes[-1], len(shapes) * width + next_step, 0, width, height)

  elif(letter == 'b'):
    draw_b(shapes[-1], len(shapes) * width + next_step, 0, width, height)

  elif(letter == 's'):
    draw_s(shapes[-1], len(shapes) * width + next_step, 0, width, height)

screen.onkeyrelease(remove_letter, 'BackSpace')

characters = ['a', 'b', 's']
for key in characters:
  screen.onkeyrelease(lambda key = key: type_letter(key), key)

screen.listen()
screen.mainloop()
