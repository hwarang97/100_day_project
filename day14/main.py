from game_data import data
import random
import art


def pick_another(person_a):
    person_b = person_a
    while person_a == person_b:
        person_b = random.choice(data)

    return person_b

def display_screen(person_a, person_b, score):
    # print log
    print(art.logo)

    # print compare A
    print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}")

    # print score
    if score > 0:
        print(f"You're right! Current score: {score}.")

    # print vs
    print(art.vs)

    # print compare B
    print(f"Compare B: {person_b['name']}, {person_b['description']}, from {person_b['country']}")

def is_correct(user_pick, person_a, person_b):
    if user_pick == 'a':
        return person_a['follower_count'] >= person_b['follower_count']
    elif user_pick == 'b':
        return person_a['follower_count'] <= person_b['follower_count']

    return False

def display_ending(is_game_over):
    if is_game_over:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")


is_game_over = False
person_b = random.choice(data)
score = 0
while not is_game_over:

    # pick another
    person_a = person_b
    person_b = pick_another(person_a)

    # display screen
    display_screen(person_a, person_b, score)

    # read input
    user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()

    # clear screen
    print("\n" * 20)

    # compare
    answer = is_correct(user_pick, person_a, person_b)

    # score update
    score += 1 if answer else 0

    # check game_over
    is_game_over = not answer

    # display_ending
    display_ending(is_game_over)
