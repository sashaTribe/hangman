import random 

class Hangman:

    def __init__(self,word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_lives = num_lives
        self.num_letters = 0
        self.list_of_guesses = []

        