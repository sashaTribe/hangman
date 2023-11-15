import random 
word_list = ['blackberry','apple','cherry','mango','orange']

class Hangman:
    '''
    This class is used to present the Hangman Game.

    Attributes:
    word_list (list of str): Lists of my 5 favourite fruits
    num_lives (int): number of lives the user has to play the game
    word (str): The word the user guesses the letters of 
    word_guessed (list of char): A list of '_' where each of those represents a letter 
    num_letters (int): Represents the number of letters left to guess
    list_of_guesses (list of char): A list that stores the guesses the user has made
    '''
    def __init__(self,word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for letter in range(len(self.word))]
        self.num_letters = len(self.word)
        self.list_of_guesses = []

    def __check_guess(self,guess):
        ''' 
        This function is used to check if the letter guessed is in the word

        Args: 
            guess (char): the guessed letter from user
        '''
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
        '''
        Get's input from user and checks it's validity.
        '''
        
        while True:
            print(self.word_guessed)
            print(f"Number of letters left: {self.num_letters} ")
            guess = input("Guess the letter: ")
            if len(guess) > 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.word_guessed:
                print("You already tried that letter!")
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)
                break



def play_game(word_list):
    '''
    This calls the hangman game and keeps running the functions until either
    no lives are left or no more letters to guess.

    Args:
        word_list (list of str): List of words the Hangman game will randomly choose
                                    one word
    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost the game")
            break
        else: 
            if game.num_letters > 0:
                game.ask_for_input()
            elif game.num_letters == 0:
                print(game.word_guessed)
                print("Congratulations. You won the game!")
                break
            else:
                pass
    


play_game(word_list)