# Python program to find roots of quadratic equation
import math


# function for finding g
def findGFromPendulum(l, T, ocillations):
    z = b / c
    x = 4 * math.pi** 2
    print((x * a) / z ** 2)

def findSwingTimeMathPendulum(l):
    print ("Wip")


# input equation
print("choose calculation")
choice = int(input())

if choice == 1:
    print("enter value for length")
    global l
    l = float(input())
    print("enter value for time")
    global T
    T = float(input())
    print("enter value for ocillations")
    global ocillations
    ocillations = float(input())

    print(findGFromPendulum(l, T, ocillations))

elif choice == 2:
    print("enter value for l")
    global l
    l = float(input())
    print (findSwingTimeMathPendulum(a))

elif choise == 0:
    print("ending .py file")
quit()