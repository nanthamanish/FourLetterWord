<h1 align="center">Four Letter Word Game</h1>

This is a basic Python module to emulate a word game on the Command Line Interface. It uses a graph whose nodes are four letter words and the edges connect two words which differ by exactly one character.

## Rules:
+ The game starts with the user choosing a four letter word.
+ Then at each turn, the opponent chooses a four letter word that differs from the previous four letter word EXACTLY by one character and has not been played before
+ Example:
   - For example, let **word** be picked first, Then the opponent can play **wore** or **work** or **ward** among the many options available.
        - **warq** is invalid as it is not a word
        - **ware** is invalid as it differs by 2 characters
    - If the opponent picks **work**, **word** cannot be picked again as it has already been played
  
## Gameplay:
+ At your turn, type in the word of your choice (case insensitive)
+ Type **resign** to quit the game (computer wins)
+ Type **Exit Game** to exit the game (game stops)
+ The computer accepts defeat if it has no options to choose from.

## Playing:
+ Run `python play_game.py` in your computer to play the game

### Files:
+ `play_game.py` - Interface for user
+ `emulator.py` - Contains class and functions required for emulation
+ `rules.txt` - Contains rules
+ `word_alpha.txt` - List of all English words (from https://github.com/dwyl/english-words)

