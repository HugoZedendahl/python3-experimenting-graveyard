import math

print("mata in radie")
radie = float(input())
print("mata in höjd")
höjd = float(input())
pi = math.pi

def volymSfär():
    resultat = (4*pi*(radie**3))/3
    print("volym av sfär =",resultat)

def ytaSfär():
    resultat = (4*pi*(radie**2))
    print("yta av sfär =",resultat)

def volymCylinder():
    resultat = pi*radie*höjd
    print("volym av cylinder",resultat)

def ytaCylinder():
    resultat = 2*pi*radie*(radie+höjd)
    print("yta av cylinder =",resultat)


volymSfär()
ytaSfär()
volymCylinder()
ytaCylinder()