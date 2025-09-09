#import random
#import string
#the code in comments are for testing purposes
matrix = []
wordList = open("svenskaOrd.txt", "r").readlines()
outputList  = []
specialOutputList = []
while True:
    inputLetters = input("Nian: ")
    #def random_char(y):
    #    return ''.join(random.choice(string.ascii_letters) for x in range(y))
    #found this method to generate test strings here https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
    #inputLetters = random_char(9)
    if len(inputLetters) == 9:
        try:
            inputLetters = str.lower(inputLetters)
            break
        except :
            print("Fel: ogiltiga tecken, försök igen.")
    elif len(inputLetters) > 9:
        print("Fel: för många bokstäver, försök igen.")
    else:
        print("Fel: för få bokstäver, försök igen.")
matrix = list(inputLetters)
specialLetter = matrix[4]
for x in wordList:
    matches = 0
    for y in matrix:
        if y in x:
            matches += 1
    if x.count(specialLetter) > 0 and 9 > matches > 4:
        outputList.append(x.strip())
    elif x.count(specialLetter) > 0 and matches == 9:
        specialOutputList.append(x.strip())
for z in outputList:
    print(z)
print("")
print(len(specialOutputList)," ord som använder alla bokstäver:")
for zz in specialOutputList:
    print(zz)