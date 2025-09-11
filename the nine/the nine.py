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
    word = x.strip()
    currentWord = list(word)
    if 4 <= len(currentWord) <= 8 and all(letter in matrix for letter in currentWord) and specialLetter in currentWord:
        outputList.append(word)
    elif sorted(currentWord) == sorted(matrix):
        specialOutputList.append(word)

for z in outputList:
    print(z)
print("")
print(len(specialOutputList)," ord som använder alla bokstäver:")
for zz in specialOutputList:
    print(zz)


# asw
# fde
# lkg