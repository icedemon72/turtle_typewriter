import turtle

def draw_a(turtle_object, y_start_coordinate = 0, x_start_coordinate = 0, letter_width = 25, letter_height = 50):
  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate, y_start_coordinate)
  turtle_object.pendown()
  
  turtle_object.setpos(x_start_coordinate + (letter_width / 2), y_start_coordinate + letter_height)
  turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate)
 
  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate + letter_width - (letter_width * 0.2), y_start_coordinate + letter_height * 0.4)
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate + (letter_width * 0.2), y_start_coordinate + letter_height * 0.4)

  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate + (letter_width * 1.1), y_start_coordinate)
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate + (letter_width * 0.9), y_start_coordinate)

  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate - (letter_width * 0.1), y_start_coordinate)
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate + (letter_width * 0.1), y_start_coordinate)
  turtle_object.hideturtle()

def draw_b(turtle_object, y_start_coordinate = 0, x_start_coordinate = 0, letter_width = 25, letter_height = 50):
  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate, y_start_coordinate)
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate, y_start_coordinate + letter_height)
  turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate + letter_height)
  turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate + (letter_height * 0.9))

  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate, y_start_coordinate + (letter_height / 2))
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate + (letter_width / 2), y_start_coordinate + (letter_height / 2))

  turtle_object.penup()
  turtle_object.setpos(x_start_coordinate, y_start_coordinate)
  turtle_object.pendown()

  turtle_object.setpos(x_start_coordinate + (letter_width / 2), y_start_coordinate)
  turtle_object.circle((letter_width / 2), 180)
  turtle_object.hideturtle()
  turtle_object.hideturtle()
