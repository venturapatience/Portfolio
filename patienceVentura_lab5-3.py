# patience ventura 13 Feb 2025 patienceVentura_lab5-3.py
'''
This program utilizes the turtle module to draw a snowman with a scarf.
'''

import turtle

# Global constants
ANIMATION_SPEED = 0
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
PEN_WIDTH = 2

# Setup the window.
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Define Functions
def main():
    turtle.speed(ANIMATION_SPEED)
    turtle.hideturtle()
    turtle.pensize(PEN_WIDTH)
    drawBase(0, -150, 100)
    drawMidSection(0, 25, 75)
    drawHead(0, 150, 50)
    drawHat()
    drawArms()
    drawScarf()

    # Keep window open
    turtle.done()

def drawBase(x, y, radius):
    drawCircles(x, y, radius)

def drawMidSection(x, y, radius):
    drawCircles(x, y, radius)

def drawHead(x, y, radius):
    drawCircles(x, y, radius)

    # Draw Face: Eyes and Mouth
    drawCircles(-20, 155, 7)
    drawCircles(20, 155, 7)
    drawLine(-30, 130, 30, 130)

def drawHat():
    drawRectangle(-75, 180, 150, 20)
    drawRectangle(-45, 190, 90, 60)

def drawArms():
    # Draw Left Arm
    drawLine(-75, 25, -120, 35)
    drawLine(-120, 35, -130, 100)
    drawLine(-130, 100, -125, 110)
    drawLine(-130, 100, -140, 105)

    # Draw Right Arm
    drawLine(75, 25, 140, 80)
    drawLine(140, 80, 145, 100)
    drawLine(140, 80, 160, 80)

def drawScarf():
    # Draw First part of scarf (the horizontal one around neck)
    turtle.penup()
    turtle.goto(-35, 110)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(-15, extent = -150)
    turtle.setheading(-30)
    turtle.circle(100, 50)
    turtle.setheading(10)
    turtle.circle(15, extent = 150)
    turtle.setheading(-170)
    turtle.circle(-150, 30)
    turtle.end_fill()

    # Draw Second part of scarf (the dangling part of scarf)
    turtle.penup()
    turtle.goto(-20, 72)
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.setheading(230)
    turtle.circle(60, extent=50)
    turtle.setheading(-30)
    turtle.circle(30, extent=40)
    turtle.setheading(-80)
    turtle.circle(60, extent=-50)
    turtle.setheading(-180)
    turtle.circle(-40, 28)
    turtle.end_fill()

# Common geometric shapes

def drawCircles(x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.circle(radius)

def drawLine(startX, startY, endX, endY):
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.pendown()
    turtle.goto(endX, endY)

def drawRectangle(x, y, width1, width2, color = 'black', angle = 90):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width1)
        turtle.left(angle)
        turtle.forward(width2)
        turtle.left(angle)
    turtle.end_fill()

# Call the main function
if __name__ == '__main__':
    main()


