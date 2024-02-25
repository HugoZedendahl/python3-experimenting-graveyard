import math
import time

var1 = 5
var2 = 25 
#våra tal
addSum = int(var2) + int(var1)
subSum = int(var2) - int(var1)
divSum = var2/var1
mulSum = var2*var1

# addera, subtraherar, dividerar och multiplicerar värde2 med värde 1 i denna ordning

print(addSum)
print(subSum)
print(divSum)
print(mulSum)

#printar alla resultat

if var2 == 20:
    print(var2," är 20")
elif var2 < 20:
    print(var2," är mindre än 20")
elif var2 > 20:
    print(var2," är större än 20")

#kollar ifall var2(25) är lika med, är mindre eller är större i den ordningen, och ger ett svar i varje fall. 

var3 = 256
sqrtOfVar3 = math.sqrt(var3)

#tar 256 och drar roten ur talet
print(sqrtOfVar3)

#visar resultatet av roten
pi = math.pi
cosOfPi = math.cos(pi)

#tar pi och räknar cosinus av pi

print(cosOfPi)

#printar resultatet av cos of pi

print(time.time())
time.sleep(5)
print(time.time())

#printar tiden i sekunder sedan jan1 1970 (utc)