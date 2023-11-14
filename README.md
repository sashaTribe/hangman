# Hangman

## Description
This is an implementation of a game of Hangman in Python. It guesses a letter that may be in a selected word. If the letter is in the selected word, the user is safe. If the letter is invalid, the user is one step closer to being hanged.
So far it takes in a letter of the user and checks whether it is valid (if it is actually a letter), and will continuously ask user for a letter if the user carries on typing in an invalid character. After that, it checks if the valid input is in the word, if it is then a message will be sent out saying it is in the word, if not then it will ask to try again.
The short-term aim is to create method that keeps track on how many mistakes the user makes.
## File Structure
- milestone_2.py