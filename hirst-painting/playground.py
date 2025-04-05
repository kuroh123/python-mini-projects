from turtle import Turtle, Screen
import random

cal = Turtle()
cal.shape('turtle')
cal.color('CadetBlue')

def draw_square(side_len, no_of_sides):
    i = 0
    while i < no_of_sides:
        cal.forward(side_len)
        cal.right(90)
        i += 1

def draw_dotted_line():
    for i in range(5):

        cal.pendown()
        cal.forward(10)
        cal.penup()
        cal.forward(10)

def draw_all_shapes(side_len):
    for i in range(3, 11):
        r = random.random()
        g = random.random()
        b = random.random()
        cal.pencolor(r, g, b)
        angle = 360 / i
        j = 0
        while j < i:
            cal.forward(side_len)
            cal.right(angle)
            j += 1
        i += 1

def draw_random_lines(side_len, no_of_lines):
    cal.pensize(10)
    cal.speed('fastest')
    directions = [0, 90, 180, 270]
    for _ in range(no_of_lines):
        r = random.random()
        g = random.random()
        b = random.random()
        cal.pencolor(r, g, b)
        direction = random.choice(directions)
        cal.setheading(direction)
        cal.forward(side_len)

def draw_spirograph(radius):
    cal.speed('fastest')
    tilt = 0
    while tilt != 360:
        r = random.random()
        g = random.random()
        b = random.random()
        cal.pencolor(r, g, b)
        cal.setheading(tilt)
        cal.circle(radius)
        tilt += 10

# draw_dotted_line()
# draw_square(100, 4)
# draw_all_shapes(50)
# draw_random_lines(20, 100)
draw_spirograph(50)
screen = Screen()
screen.exitonclick()
