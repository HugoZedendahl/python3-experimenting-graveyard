matrix = ([],[],[])
wordList = open("svenskaOrd.txt", "r").readlines()
while True:
    inputLetters = input("Nian: ")
    if inputLetters.conunt() == 9:
        inputLetters = str.lower(inputLetters)
        break
    elif inputLetters.conunt() > 9:
        print("Fel: för många bokstäver, försök igen.")
    else:
        print("Fel: för få bokstäver, försök igen.")

matrix[0] = list(inputLetters[0:3])
matrix[1] = list(inputLetters[3:6])
matrix[2] = list(inputLetters[6:9])
specialLetter = matrix[1][1]

print(wordList)