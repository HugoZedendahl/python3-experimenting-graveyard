mode = None
tempInput = None
avTrains = ["dest 1","dest 2","dest 3"]
genderOptions = ["man","woman","other"]
bookings = {
    "person 1":["dest 1","dest 2","man",24],
    "person 2":["dest 1","dest 3","woman",60],
    "person 3":["dest 2","dest 1","other",50],
}

def booking():
    print("select destination:")
    print("1 for dest 1, 2 for dest 2, 3 for dest3.")
    try:
        destination = avTrains[(int(input())-1)]
    #adjusting for python indexing
    except:
        print("out of range, no destination with that designation, please try again")
        return
    print("select departure location, this cannot be the same as your destination")
    try:
        departure = avTrains[(int(input())-1)]
        if departure == destination:
            print("can't book to and from the same location, please try again")
            return
    #adjusting for python indexing, checks if the destination is the same as the departure location
    except:
        print("out of range, or no destination with that designation, please try again")
        return
    print("enter name of traveller:")
    try:
        traveller = str(input())
    except:
        print("significant type error, contact admin")
        return
    #entering a name in the form of a string to be used as a keyvalue
    print("enter gender:")
    print("1 for man, 2 for woman, 3 for other")
    try:
        gender = genderOptions[(int(input())-1)]
    except:
        print("not in range, please try again")
        return
    #entering gender from options
    print("enter age")
    try:
        age = int(input())
    except:
        print("not a valid age, please try again")
        return
    #entering age in the form of a integer
    try:
        if traveller not in bookings.keys():
            bookings.update({traveller:[departure,destination,gender,age]})
    except:
        print("booking operation error, if person already booked try unbooking and booking again")
        return
    #updates the booking dictionary, if person already booked, rejects input

print("welcome to python-no-interaface trains, less ui, cheaper tickets!")
while True:
    print("select operation:")
    print("1 to book, 2 to cancel, 3 to show available ticket locations, 4  to quit")
    try:
        mode = int(input())
    except:
        print("not a option, please try again")

    if mode == 1:
        booking()
    #booking function
    elif mode == 2:
        print("please enter the name of the passanger, this is case sensetive")
        try:
            tempInput = str(input())
            justDeleted = bookings.pop(tempInput)
            print(tempInput," ",justDeleted," avbokad")
        #takes the input, shows who got cancelled, info about them
        except:
            print("this is case sensetive, or a operations error occured. please try again")
    
    elif mode == 3:
        print("available stations are")
        print(avTrains)

    elif mode == 4:
        print("see you soon")
        quit()
    #debug statement below. uncomment for operation
    #elif mode == 5:
    #    print(bookings)   