# patience ventura  2025Jan31  patienceVentura_lab3-3.py
'''

This program is a little game that asks the user to input an angle and a force to launch a projectile
and determine if the projectile hit the target or not. The program also provides feedback to the user
on how to adjust the angle and force to hit the target.

'''

# Hit the Target Game
import turtle

# Named constants
SCREEN_WIDTH = 600    # Screen width
SCREEN_HEIGHT = 600   # Screen height
TARGET_LLEFT_X = 100  # Target's lower-left X
TARGET_LLEFT_Y = 250  # Target's lower-left Y
TARGET_WIDTH = 25     # Width of the target
FORCE_FACTOR = 30     # Arbitrary force factor
PROJECTILE_SPEED = 1  # Projectile's animation speed
NORTH = 90            # Angle of north direction
SOUTH = 270           # Angle of south direction
EAST = 0              # Angle of east direction
WEST = 180            # Angle of west direction

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw the target.
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# Center the turtle.
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force inputs from the user.
angle = turtle.numinput('Angle Input Needed', "Enter the projectile's angle (0-359): ", minval=0, maxval=359)
force = turtle.numinput('Force Input Needed', "Enter the launch force (1-10): ", minval=1, maxval=10)

# Calculate the distance.
distance = force * FORCE_FACTOR

# Set the heading.
turtle.setheading(angle)

# Launch the projectile.
turtle.pendown()
turtle.forward(distance)

# ==================== Output the result. ====================
# Did it hit the target?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target hit!')

# === Let user know the target is in the first quadrant of Cartesian plane ===
elif angle >= NORTH:
        print('Try a smaller angle.')

# === divide the surroundings of the target into 8 quadrants ===

# Quadrant 1: Lower right of the target (bottom right corner)
elif (turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor() < TARGET_LLEFT_Y):
        print('Try a larger angle.')
        print('Use greater force.')

# Quadrant 2: Right side of the right part of target (right side)
elif (turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Try larger angle.')

# Quadrant 3: Upper right of the target (top right corner)
elif (turtle.xcor() > (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Try larger angle.')

# Quadrant 4: Upper side of the top part of target (top side)
elif (turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Use less force.')

# Quadrant 5: Upper left of the target (top left corner)
elif (turtle.xcor() < TARGET_LLEFT_X) and (turtle.ycor() > (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Try a smaller angle.')

# Quadrant 6: Left side of the left part of target (left side)
elif (turtle.xcor() < TARGET_LLEFT_X) and (turtle.ycor() >= TARGET_LLEFT_Y and turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Try a smaller angle.')

# Quadrant 7: Lower left of the target (bottom left corner)
elif (turtle.xcor() < TARGET_LLEFT_X) and (turtle.ycor() < TARGET_LLEFT_Y):
        print('Try a smaller angle.')
        print('Use greater force.')

# Quadrant 8: Lower side of the bottom part of target (bottom side)
elif (turtle.xcor() >= TARGET_LLEFT_X and turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH)) and (turtle.ycor() < TARGET_LLEFT_Y):
        print('Use greater force.')

else:
        print('You missed the target.')

# Keep window open
turtle.done()