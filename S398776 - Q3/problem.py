import turtle
import math

# ---------------- Recursive Function ----------------
def inward_koch(t, length, depth):
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

# ---------------- Draw Polygon ----------------
def draw_polygon(t, sides, length, depth):
    angle = 360 / sides
    for _ in range(sides):
        inward_koch(t, length, depth)
        t.right(angle)

# ---------------- MAIN PROGRAM ----------------
def main():
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
    
    # Center the polygon
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

