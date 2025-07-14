# patience ventura  2025Jan23  patienceVentura_lab2-3.py

'''

This program utilizes turtle graphics to draw two shapes shown in the textbook.
The first shape is the top left figure, which is two side-by-side diamonds.
The second shape is the middle left figure, which is a rectangular prism.

'''

# Importing turtle graphics
import turtle

# Set the window size
turtle.setup(1200,600)

# Set up the turtle
turtle.hideturtle()
turtle.pensize(3)

# === Create named constants for coordinates ===

# For first shape
DIAMOND_CENTER_X = -300
DIAMOND_CENTER_Y = 0

# For second shape
PRISM_LEFT_X = 200
PRISM_CENTER_X = 300
PRISM_RIGHT_X = 400

PRISM_UPPER_Y = 100
PRISM_CENTER_Y = 0
PRISM_LOWER_Y = -100


# ============= SHAPE #1: Side-by-side Diamonds =================

# Go to the left side of the screen for first shape
turtle.penup()
turtle.goto(DIAMOND_CENTER_X, DIAMOND_CENTER_Y)

# Draw the diamond on the right
turtle.pendown()
turtle.left(45)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(150)

# Draw the diamond on the left
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)


# ============= SHAPE #2: Rectangular Prism =================

# === Go to the right part of the screen for second shape ===
turtle.penup()
turtle.goto(PRISM_CENTER_X, PRISM_UPPER_Y)

# === Draw upper left square ===
turtle.pendown()
turtle.setheading(270)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# === Draw lower right square ===

turtle.penup
turtle.goto(PRISM_CENTER_X, PRISM_CENTER_Y)

turtle.setheading(270)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# === Draw diagonal lines ===

# Diagonal 1: Lower left
turtle.penup()
turtle.goto(PRISM_CENTER_X, PRISM_LOWER_Y)
turtle.pendown()
turtle.goto(PRISM_LEFT_X, PRISM_CENTER_Y)

# Diagonal 2: Upper right
turtle.penup()
turtle.goto(PRISM_RIGHT_X, PRISM_CENTER_Y)
turtle.pendown()
turtle.goto(PRISM_CENTER_X, PRISM_UPPER_Y)

# Diagonal 3: Long diagonal in the "middle"
turtle.penup()
turtle.goto(PRISM_RIGHT_X, PRISM_LOWER_Y )
turtle.pendown()
turtle.goto(PRISM_LEFT_X, PRISM_UPPER_Y)



# === Keep the window open ===

turtle.done()