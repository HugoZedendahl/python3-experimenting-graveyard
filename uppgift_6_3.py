import random
mainLoopActive = True
gInputActive = True
aInputActive = True
cont = True
category = None 
M1 = None
M2 = None
A1 = 6
A2 = 6
G1 = random.randint(1,100)+random.randint(1,100)+random.randint(1,100)+random.randint(1,100)+random.randint(1,100)
G2 = random.randint(1,100)+random.randint(1,100)+random.randint(1,100)+random.randint(1,100)+random.randint(1,100)
#adds small random numbers to simulate a database
#all variables are named after the flowchart when possible
print("welcome to the avaragator, we avarage ages of people")
print("please add a person to the database")

while mainLoopActive == True:
    #starts the main database entry loop 
    cont = True
    #add this here so upon adding more pepole we dont get stuck in a endless loop
    input
    while gInputActive == True:
        print("is the person we are entering a man or a woman?")
        print("1 for man, 2 for woman")
        try:
            category = int(input())
            if category == 1 or category ==2:
                gInputActive = False
            else:
                print("please enter 1 or 2")
        except:
            print("not an option, try again")
    #checks the catefory and where to add people
    while aInputActive == True:
        print("what is the persons age?")
        try:
            age = int(input())
            if category == 1:
                A1 += 1
                G1 += age
            elif category == 2:
                A2 += 1
                G2 += age
            aInputActive = False
        except:
            print("not a valid input, please try again")
    #adds to the database
    while cont == True:
        print("add more people? 1 for yes. 2 for no.")
        try:
            category = int(input())
            if category == 1:
                gInputActive = True
                aInputActive = True
                cont = False
            #resets our input loop
            elif category == 2:
                mainLoopActive = False
                cont = False
            #sets the input loop and this loop comdition to false breaking it on completion
            else:
                print("out of range, please only use one or two")
            #if someone puts some garbage into this
        except:
            print("please only enter 1 or 2")
            #if someone tries to enter wierd data
#below are the end  prosseces as given in the assignent
M1 = G1/A1

print(f"there are {A1} men in the database wih a avarage age of {M1}")

M2 = G2/A2

print(f"there are {A2} women in the database wih a avarage age of {M2}")

print("thank you for contributing to the avaragator")

quit()