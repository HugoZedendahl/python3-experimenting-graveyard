import random
#uppgift 5,1 gissa nummret
ranVar = None
guess = None

while True:
    ranVar = random.randint(1,9)
    #genererar ett nummer för os att gissa, detta slumpas mellan varje iteration, för att få ett nummer som inte slumpas mellan varje gissning flytta "random.randint(1,9)" till ranVar definitionen utanför denna while loop på rad 3
    print("""gissa ett nummer mellan 0 och 10, eller "quit" för att avsluta""")
    userInput = input()
    #ger instructioner för detta program och väntar på användaren
    if userInput == "quit":
        print("avslutar program")
        quit()
    #ett sätt att avsulta programmet för både test syften och ifall man bara vill avsluta programmet
    try:
        guess = int(userInput)
        if guess == ranVar:
            print("rätt nummer!")
            break
        else:
            print("fel nummer!")
        #ser till att guess variabeln är en integer och sedan checkar av den emot vår genererade variabel. ifall det är fel, bryter inte loopen och låter den fortsätta
    except:
        print("inte ett nummer, skriv ett nummer och försök igen")
    #ifall användaren matar in ett värde som inte kan bli tolkat som en integer sä är denna try/except funktion vårt sätt att undvika en krash