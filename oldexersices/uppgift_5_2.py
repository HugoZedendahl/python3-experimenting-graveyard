heltal = None
summa = None
iterations = 0
tempInput = None
#definierar variables som programmet kommer att arbeta med

def multiply(x):
    heltal = None
    summa = x
    iterations = 1
    while summa<=99:
        iterations += 1
        summa += x
    print(f"{x} needed to be multiplied by {iterations} to reach above a hundred with a final value of {summa}")
#kodblocket som kommer att multiplicera ett tal tills det når ett värde av 100 eller mer
while True:
    print("""input the integer you want multiplied, or write "quit" to quit""")
    tempInput=input()
    #input för användarinmating
    if tempInput == "quit":
        break
    #funktion för att avsluta programmet
    try:
        multiply(int(tempInput))
    except:
        print("not a integer, please enter a integer value")
        continue
    #försöker att multiplicera, ifall det inte är ett tal, informerar och passerar