var = "1966grundade456for789data"
numVar = ""
sumVar = 0
numVarPlus =""
for x in var:
    if x.isdigit():
        numVar = numVar + x
        sumVar += int(x)

for x in numVar:
    numVarPlus = numVarPlus + " + " + x

print(f"alla nummer i {var} är {numVar}")
print(numVarPlus.strip(" + "),"=",sumVar,)