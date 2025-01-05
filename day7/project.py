word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

import random

stages = [r'''
 +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
 +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
 +---+
  |   |
  O   |
 /|   |
      |
      |
========
''', r'''
 +---+
  |   |
  O   |
  |   |
      |
      |
========
''', r'''
 +---+
  |   |
  O   |
      |
      |
      |
========
''', r'''
 +---+
  |   |
      |
      |
      |
      |
''']


chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ["_"] * len(chosen_word) # similar to str, but access element by index
lives = 6

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
    else:
        for idx, letter in enumerate(chosen_word):
            if guess == letter:
                placeholder[idx] = letter

    print(stages[lives])
    guess_str = "".join(placeholder)
    print(guess_str)

    if "_" not in placeholder:
        game_over = True

    if lives == 0:
        game_over = True
        print("You lose!")
