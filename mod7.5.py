# Alinura Sultanova
# 08.17.2023

#Problem 5

import turtle

def drawSquare(t, sz):
    """
    Get turtle t to draw a square of side length sz.
    
    Parameters:
    t (turtle.Turtle): The turtle used for drawing.
    sz (int): The side length of the square.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)

# Set up the screen and turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("blue")

# Call the function to draw a square
drawSquare(alex, 100)  # Drawing a square with side length 100

wn.exitonclick()  # Close the window when clicked
