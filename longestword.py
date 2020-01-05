listOfWords = []
numberOfLetters = 0
n = int(input("Number of words: "))
print("Enter the words")
for i in range(0,n):
   ele = input()
   listOfWords.append(ele)
   if len(ele) >= numberOfLetters:
       numberOfLetters = len(ele)
       word = ele
print(listOfWords)
print("Longest word: ", word)
print("Length : ", numberOfLetters)