import turtle
import math

# ---------------- Recursive Function ----------------
def inward_koch(t, length, depth):
    if depth == 0:
        t.forward(length)