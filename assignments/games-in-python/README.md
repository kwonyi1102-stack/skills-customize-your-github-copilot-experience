
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, random selection, and user input while creating a complete playable program.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description

Complete the game setup so that each round selects a secret word and initializes the variables needed to track the player's progress.

#### Requirements

Completed program should:

- Randomly select one word from the predefined `words` list.
- Store guessed letters and the number of incorrect guesses.
- Set a maximum number of incorrect guesses before the player loses.

### 🛠️ Implement Guessing and Game Results

#### Description

Implement the main game loop. Ask the player for letter guesses, reveal correctly guessed letters, update incorrect guesses, and finish the game with the appropriate result.

#### Requirements

Completed program should:

- Accept letter guesses and display the current word progress using underscores, such as `_ _ _`.
- Track and display the number of incorrect guesses remaining.
- End when the player guesses the complete word or runs out of attempts.
- Display a clear win message or lose message at the end of the game.
