from art import logo
import random


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
DIFFICULTY_LEVELS = {"easy" : EASY_LEVEL_TURNS, "hard" : HARD_LEVEL_TURNS}


def compare(guess: int, actual_answer: int):
    """Compare guess with actual_answer and print result"""
    if guess == actual_answer:
        print(f"You got it! The answer was {answer}.")
    else:
        if guess > actual_answer:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")


def set_difficulty():
    """set difficulty, initial attempts and return initial attempts"""
    while True:
        difficulty_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
        try:
            initial_attempts = DIFFICULTY_LEVELS[difficulty_input]
            return initial_attempts
        except KeyError:
            print(f"Invalid difficulty: {difficulty_input}")


print(logo)
print("""
    Welcome to the Number Guessing Game!\n
    I'm thinking of a number between 1 and 100. 
""")

remaining_attempts = set_difficulty()
answer = random.randint(1,100)

is_game_over = False
choice = -1
while not is_game_over:

    choice = int(input(f"You have {remaining_attempts} attempts remaining to guess the number.\nMake a guess: "))
    remaining_attempts -= 1

    if remaining_attempts > 0:
        compare(choice, answer)

    if remaining_attempts == 0 or choice == answer:
        is_game_over = True

if remaining_attempts == 0:
    print("print You've run out of guess.\nRefresh the page to run again.")

