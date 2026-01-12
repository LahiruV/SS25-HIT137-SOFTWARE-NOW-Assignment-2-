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
