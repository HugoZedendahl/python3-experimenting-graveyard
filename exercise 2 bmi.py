vikt = input("vikt i kg: ")
längd = input("längd i meter: ")
try:
    bmi = int(vikt) / float(längd) ** 2
except ValueError:
    print("bad data type")
try:
    if 0 < bmi < 18.5:
        print("undervikt")
    elif 18.5 <= bmi < 25:
        print("normalvikt")
    elif 25 <= bmi < 30:
        print("övervikt") 
    elif bmi :
        print("grov övervikt")
    elif bmi < 0:
        print("ej korrekt värde")
    else :
        print("hur fan kom du hit?")
except ValueError:
    print("bad data type") 