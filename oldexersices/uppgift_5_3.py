choice = 0
#variabel för att lagra input
while True:

    print("""select option, "1" for introducions, "2" for your age and "3" to quit""")
    try:
        choice = int(input())
    except:
        "not a option, my deepest apologies good sire"
    #lagrar input som en int
    if choice==1:
        print("greetings humble wizard")
    elif choice==2:
        print("how old where you now again?")
        age = int(input())
        print(f"ah yes you are {age} years old")
    elif choice==3:
        print("buh-bye")
        quit()
    #alternativen