# patience ventura 2025February06 patienceVentura_lab4-3.py
'''
This program utilizes the turtle module to draw repeating squares using loops.
'''

# Repeating Squares
import turtle

# Named constants
ANIMATION_SPEED = 0
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270
X_INITIAL = 250
Y_INITIAL = -250

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Setup the turtle
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Move the turtle to the initial position. The programmer chose this initial position
# so that the squares will be drawn starting from the lower right corner of the screen
# in case the user wants to draw a large number of squares or input a large length increase

turtle.penup()
turtle.goto(X_INITIAL, Y_INITIAL)

# Get input from user about the desired design of the square

first_length = int(turtle.numinput('Input First Length', 
                                   'Please enter the length of the first line of the square: '))
length_increase = int(turtle.numinput('Input Length Increase', 
                                      'Please enter the length increase after each square is drawn: '))
num_square = int(turtle.numinput('Input Number of Squares', 
                                 'Please enter the number of squares to draw: '))

# Draw the circles using a for loop

for count in range(num_square):
    turtle.pendown()

    turtle.setheading(NORTH)
    turtle.forward(first_length)

    turtle.setheading(WEST)
    turtle.forward(first_length)

    turtle.setheading(SOUTH)
    turtle.forward(first_length)

    turtle.setheading(EAST)
    turtle.forward(first_length)

    # Update the length of the square for each iteration
    first_length = first_length + length_increase

# Keep window open
turtle.done()