toDoList = ["these","are","temp","values"]
justDeleted = None
tempInput = None
#our variables

def addToDo(x):
    toDoList.append(x)
    print("added assignment")
#function to add to todo list

def markToDoDone(x):
    x = x-1
    toDoList[x] = toDoList[x]+" (done)"
    print ("marked as complete")
#function to mark assignemnt as done, with the index adjusted for user usability

def showAllToDo():
    print(toDoList)
#show the todolist

def removeToDo(x):
    x = x-1
    justDeleted = toDoList[x]
    del toDoList[x]
    print("you just Deleted",justDeleted)
#remove a indexed number, with the index adjusted for user usability

print("welcome to the todolist!")
while True:
    print("use 1 to add, 2 to mark as done, 3 to remove a entry, 4 to display list 5 to quit, please only use numbers for mode selection")
    try:
        mode = int(input())
    except:
        print("NaN")
    #chooses the mode of operation
    if mode == 1:
        print("please write assignment to add")
        addToDo(str(input()))
    #adds a value to the list
    elif mode == 2:
        print("please choose the number of what you want to mark as done")
        try:
            markToDoDone(int(input()))
        except:
            print("not in range")
    #marks a thing as done
    elif mode == 3:
        print("select what entry to delete")
        try:
            removeToDo(int(input()))
        except:
            print("not in range")
    #deletes a entry
    elif mode == 4:
        showAllToDo()
    #shows the todolist
    elif mode == 5:
        print("quitting application")
        quit()
    #quits the application