#from milestone_2 import hangman_word

hangman_word = "apple"

def check_guess(guess):
    guess.lower()
    if guess in hangman_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    guess = ""
    while True:
        guess = input("Guess the letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()