variableToConvert = ""
#variabeln vi vill arbeta med
while True:
    print("""skriv in en siffra, eller skriv "sluta" för att avsluta programmet""")
    variableToConvert = input()
    #input för siffra
    print("""du skrev " """+variableToConvert""" " """)
    #visar strängen

    if(variableToConvert == "sluta"):
        quit()
    else:
        try:
            variableToConvert = float(variableToConvert)
            #översätter strängen till ett flyttal
        except:
            print(""" " """variableToConvert""" " """ """"är inte ett nummer eller "sluta", försök igen""")
            continue
    #testar för att se att strängen kan bli översatt

    print(variableToConvert)
    variableToConvert = int(variableToConvert)
    #översätter flyttalet till ett heltal
    print(variableToConvert)