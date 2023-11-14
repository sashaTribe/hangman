import random


word_list = ['blackberry','apple','cherry','mango','orange']
#print(word_list)
hangman_word = random.choice(word_list)
#print(word)

user_guess = input("Type in a single letter: ")
if len(user_guess) == 1 and user_guess.isalpha():
    print("Good guess!")
else:
    print("Oops, invalid input")


lst = ['_' for i in range(3)]
print(lst)