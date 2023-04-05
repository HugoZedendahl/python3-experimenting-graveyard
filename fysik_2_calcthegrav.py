# Python program to find roots of quadratic equation
import math

l = 0
T = 0
ocillations = 0

# function for finding g
def findGFromPendulum(l, T, ocillations):
    z = T / ocillations
    x = 4 * math.pi** 2
    return((x * l) / z ** 2)

def findSwingTimeMathPendulum(l):
    return("Wip")


# input equation
print("choose calculation")
choice = int(input())

if choice == 1:
    print("enter value for length")
    l = float(input())
    print("enter value for time")
    T = float(input())
    print("enter value for ocillations")
    ocillations = float(input())

    print(findGFromPendulum(l, T, ocillations))
    print("calc done, ending .py file")

elif choice == 2:
    print("enter value for l")
    l = float(input())
    print(findSwingTimeMathPendulum(l))

elif choice == 0:
    print("ending .py file")
quit()