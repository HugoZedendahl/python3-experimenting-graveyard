# Python program to find roots of quadratic equation
import math


# function for finding roots
def equationroots(a, b, c):

    print((((4 * math.pi)** 2) * a) / (b / c))


# inputs
print("enter value for a")
a = float(input())
print("enter value for b")
b = float(input())
print("enter value for c")
c = float(input())


equationroots(a, b, c)
