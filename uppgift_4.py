import math
import time

var1 = 5
var2 = 25 

addSum = int(var2) + int(var1)
subSum = int(var2) - int(var1)
divSum = var2/var1
mulSum = var2*var1

print(addSum)
print(subSum)
print(divSum)
print(mulSum)

if var2 == 20:
    print(var2," är 20")
elif var2 < 20:
    print(var2," är mindre än 20")
elif var2 > 20:
    print(var2," är större än 20")

var3 = 256
sqrtOfVar3 = math.sqrt(var3)

print(sqrtOfVar3)

pi = math.pi
cosOfPi = math.cos(pi)

print(cosOfPi)

print(time.time())
time.sleep(5)
print(time.time())