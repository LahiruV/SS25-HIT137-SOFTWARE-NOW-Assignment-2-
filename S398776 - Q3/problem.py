"""
This program draws an inward Koch fractal pattern
inside a polygon using Python turtle graphics.
The design depends on the number of sides and
recursion depth given by the user.
"""

import turtle
import math


def inward_koch(t, length, depth):
    """
    Draws one side of an inward Koch curve.

    t      : turtle object used for drawing
    length : length of the line segment
    depth  : recursion level for the Koch pattern

    If depth is 0, it draws a straight line.
    Otherwise, it breaks the line into smaller
    parts and draws the pattern recursively.
    """
    if depth == 0:
        t.forward(length)
    else:
        length /= 3

        inward_koch(t, length, depth - 1)
        t.right(60)

        inward_koch(t, length, depth - 1)
        t.left(120)

        inward_koch(t, length, depth - 1)
        t.right(60)

        inward_koch(t, length, depth - 1)


def draw_polygon(t, sides, length, depth):
    """
    Draws a polygon where each side is
    an inward Koch curve.

    sides  : number of sides of the polygon
    length : length of each side
    depth  : recursion depth for the Koch curve
    """
    angle = 360 / sides
    for _ in range(sides):
        inward_koch(t, length, depth)
        t.right(angle)


def main():
    """
    Main function of the program.
    Takes user input, sets up the turtle screen,
    and starts drawing the fractal polygon.
    """
    # User Inputs
    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))

    # Turtle Setup
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("black")
    t.pensize(2)

    # Position turtle to center the shape
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    # Draw the fractal polygon
    draw_polygon(t, sides, length, depth)

    t.hideturtle()
    turtle.done()


# Program starts here
main()