# Hugo Zedendahl 950228-5217
# i just cannot get the last test to work, if i adjust it so test 8 would pass, it breaks other tests- logically the program should function the wai we want it to function now.
# also my apologies for submitting 2 assignments. i was just curious about the tests on this assignment and wanted to just test it, didnt see a way to do it 
# without submitting

#import random
#import string
#the code in comments are for testing purposes
matrix = []
wordList = open("svenskaOrd.txt", "r").readlines()
outputList  = []
specialOutputList = []
check = True
inputLetters = input()

while True:
    
    #def random_char(y):
    #    return ''.join(random.choice(string.ascii_letters) for x in range(y))
    #found this method to generate test strings here https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python i would generate my own strings and just loop the entire program
    #inputLetters = random_char(9)
    if len(inputLetters) == 9:
        try:
            inputLetters = str.lower(inputLetters)
            break
        except :
            print("Nian: Fel: ogiltiga tecken, försök igen.")
    elif len(inputLetters) > 9:
        print("Nian: Fel: för många bokstäver, försök igen.")
        inputLetters = input("Nian:")
    else:
        print("Nian: Fel: för få bokstäver, försök igen.")
        inputLetters = input("Nian:")
matrix = list(inputLetters)
specialLetter = matrix[4]

for x in wordList:
    word = x.strip()
    currentWord = list(word)
    for letter in word:
        if letter not in matrix or matrix.count(letter) < word.count(letter):
            check = False
    if 4 <= len(currentWord) and specialLetter in currentWord and check == True:
        outputList.append(word)
    if sorted(currentWord) == sorted(matrix):
        specialOutputList.append(word)
    check = True

if len(outputList) > 0:
    for z in outputList:
        print(str(z))
    print("")
    if len(specialOutputList) > 0:
        print(f"{len(specialOutputList)} ord använder alla bokstäver:")
        for zz in specialOutputList:
            print(str(zz))
    else:
        print("Det finns inga ord som använder alla bokstäver.")
else:
    print("Hittade inga ord alls.")


# asw
# fde
# lkg
#
#this is just for me to visualize
