import random


word_list = ['blackberry','apple','cherry','mango','orange']
#print(word_list)
word = random.choice(word_list)
#print(word)

guess = input("Type in a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops, invalid input")