import random 
word_list = ['blackberry','apple','cherry','mango','orange']

class Hangman:

    def __init__(self,word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_lives = num_lives
        self.num_letters = 0
        self.list_of_guesses = []

    def check_guess(self,guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter_index in range(len(self.word)):
                if self.word[letter_index] == guess:
                    self.word_guessed[letter_index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        #guess = ""
        while True:
            guess = input("Guess the letter: ")
            if len(guess) != 1 and guess.isnotalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.word_guessed:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

start_game = Hangman(word_list)
start_game.ask_for_input()