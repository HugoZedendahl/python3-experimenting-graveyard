# Hugo Zedendahl 950228-5217

#declaring global variables that will be used for the application
year = 0
month = 0
day = 0
monthLengthContainter = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#array for storing weekday names
weekdays =  ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "friday"]
#the main calculation for the application
def zellerCalculation(day, month, year):
    if month == 1 or month == 2:
        month += 12
        year -= 1
    weekday =(day + 13*(month+1)//5 + year + year//4 - year//100 + year//400) % 7

    print("It is a "+weekdays[weekday])
    
def inputs():
    global year
    global month
    global day
    global monthLengthContainter
    while year < 1583 or year >9999:
        year=input("Year: ")
        year=int(year)
        if year < 1583 or year >9999:
            print("Out of allowed range 1583 to 9999")
    while month < 1 or month > 12:
        month=input("Month: ")
        month=int(month)
        if month < 1 or month > 12:
            print("Out of allowed range 1 to 12")
    monthLength = monthLengthContainter[month-1]
    if year % 400 == 0 and month == 2:
        monthLength = monthLength + 1
    elif year % 4 == 0 and year % 100 != 0 and month == 2:
        monthLength = monthLength + 1
    
    while day < 1 or  day > monthLength:
        day=input("Day: ")
        day=int(day)
        if day < 1 or day > monthLength:
            print("Out of allowed range 1 to "+str(monthLength))
        

inputs()
zellerCalculation(day, month, year)  
