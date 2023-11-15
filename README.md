# Hangman

## Description
This is an implementation of a game of Hangman in Python. It prompts user to guess a letter then checks its validity, then checks whether that letter is in the randomly chosen word or not.
In terms of checks, it checks that it is:
- A single alpha character

Otherwise, it will prompt the user to retype their guess.
The game will constantly run until the user either 
- runs out of lives (that case, a message will be printed to let user know that they have lost)
- Has guessed all the correct letters (that case, a message will be printed to notify user that they have won)

Future State:
- Build a GUI for this game

What I have learnt:
- Gone more into depth with implementing an OOP application through Python
- Learnt about docstrings 

## How to run the programme
On the command line run this:
```bash
python milestone_5.py
```
## File Structure

```tree
.
├── hangman
│   ├── hangman_Template.py
│   
├── milestones
│   └── milestone_2.py
    └── milestone_3.py
    └── milestone_4.py
    └── milestone_5.py
└── README.md

```

## Examples of CLI 
### Game Won From User
![User Won](/images/game_won_example.png)

### User Lost Game
![User Lost](/images/game_lost_example.png)

### User mistyping guesses
![User Mistype](/images/mistype_response_example.png)

## License Information

This project is licensed under the [MIT License](LICENSE).