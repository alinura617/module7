# Alinura Sultanova
# 08.17.2023

# Problem 1: Write a function areaOfCircle(r) which returns the area of a circle of radius r.
Make sure you use the math module in your solution

import math  # Importing the math module to use its functions

def areaOfCircle(r):
    """
    Calculates the area of a circle given its radius.
    
    Parameters:
    r (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    area = math.pi * r**2  # Using the formula for circle's area
    return area

# Test the function
radius = 5.0
circle_area = areaOfCircle(radius)
print("The area of a circle with radius", radius, "is:", circle_area)

# finish