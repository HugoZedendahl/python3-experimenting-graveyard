import math

n = 0
secondN = 0
sum = 0
secondSum = 0
gi
#while n < 12:
#    n += 1
#    sum += 4000 + 2000 * cos(pi*n/6)
#
#print("this year", sum, "children where born")

while n < 179:
    sum += math.sin(math.radians(n))
    n += 1
    
while secondN < 179:
    secondSum += math.sin(secondN)
    secondN += 1

print("sum of the values of degrees up to 179 is", sum, "or if calculated through radians", secondSum)
