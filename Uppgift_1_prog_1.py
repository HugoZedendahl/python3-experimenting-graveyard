
variableToConvert = ""
#variabeln vi vill arbeta med
while True:
    print("skriv in en siffra, eller skriv [sluta] för att avsluta programmet")
    variableToConvert = input()
    #input för siffra
    print("du skrev "+variableToConvert)
    #visar strängen

    if(variableToConvert == "sluta"):
        quit()
    else:
        try:
            variableToConvert = float(variableToConvert)
            #översätter strängen till ett flyttal
        except:
            print("inte ett nummer eller sluta, försök igen")
            continue

    print(variableToConvert)
    variableToConvert = int(variableToConvert)
    #översätter flyttalet till ett heltal
    print(variableToConvert)