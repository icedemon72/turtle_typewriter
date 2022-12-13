from snake import snake
from turtle import *

screen = Screen()
s = snake.Snake(screen)

screen.onkeyrelease(s.delete_letter, 'BackSpace')

characters = ['a', 'b', 's']
for key in characters:
    screen.onkeyrelease(lambda key = key: s.type_letter(key), key)

screen.listen()
screen.mainloop()



steps = {"a": [
    {""}
]}