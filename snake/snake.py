import turtle


class SnakeEvent(object):
    callbacks = None

    def on(self, event_name, callback):
        if self.callbacks is None:
            self.callbacks = {}

        if event_name not in self.callbacks:
            self.callbacks[event_name] = [callback]
        else:
            self.callbacks[event_name].append(callback)

    def trigger(self, event_name):
        if self.callbacks is not None and event_name in self.callbacks:
            for callback in self.callbacks[event_name]:
                callback(self)

class Snake:

    def __init__(self, screen, width=800, height=800):
        self.shapes = []
        self.next_step = 0
        self.height = height
        self.width = width
        self.screen = screen

        self.screen.setup(width, height)

    def delete_letter(self):

        if len(self.shapes):
            self.shapes[-1].clear()
            del self.shapes[-1]

    def type_letter(self, letter):
        width = 50
        height = width * 2

        self.shapes.append(turtle.Turtle())
        self.shapes[-1].speed(0)

        if letter == "a":
            self.draw_a(self.shapes[-1], len(self.shapes) * width, 0, width, height)
        elif letter == "b":
            self.draw_b(self.shapes[-1], len(self.shapes) * width + self.next_step, 0, width, height)
        elif letter == "s":
            self.draw_s(self.shapes[-1], len(self.shapes) * width + self.next_step, 0, width, height)

    @staticmethod
    def draw_a(turtle_object: turtle.Turtle, x_start_coordinate=0, y_start_coordinate=0, letter_width=25, letter_height=50):
        turtle_object.penup()
        turtle_object.setpos(x_start_coordinate, y_start_coordinate)
        turtle_object.pendown()

        turtle_object.setpos(x_start_coordinate + (letter_width / 2), y_start_coordinate + letter_height)
        turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate)

        turtle_object.penup()
        turtle_object.setpos(x_start_coordinate + letter_width - (letter_width * 0.2),
                             y_start_coordinate + letter_height * 0.4)
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

    @staticmethod
    def draw_b(turtle_object: turtle.Turtle, x_start_coordinate=0, y_start_coordinate=0, letter_width=25, letter_height=50):
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
        turtle_object.circle((letter_width / 2), 182)
        turtle_object.hideturtle()

    @staticmethod
    def draw_s(turtle_object: turtle.Turtle, x_start_coordinate=0, y_start_coordinate=0, letter_width=25, letter_height=50):
        turtle_object.penup()
        turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate)
        turtle_object.pendown()

        turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate + (letter_height * 0.1))

        turtle_object.penup()
        turtle_object.setpos(x_start_coordinate + letter_width,
                             y_start_coordinate + letter_height - (letter_height * 0.1))
        turtle_object.pendown()

        turtle_object.setpos(x_start_coordinate + letter_width, y_start_coordinate + letter_height)
        turtle_object.right(180)
        turtle_object.circle(letter_width, 180)

