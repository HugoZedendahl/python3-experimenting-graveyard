import terminal

container = input("any number digits int: ")
container = str(container)
container = list(container)
tempContainer = 0

for x in container:
    
    tempContainer = tempContainer + int(x)

print(tempContainer)
