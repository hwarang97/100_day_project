from art import logo
import random


def calculate(cards: list) -> int:
    score = sum(cards)
    if (11 in cards) and (score > 21):
        cards.remove(11)
        cards.append(1)
        score -= 10
    return score

def take_card(cards: list, target_cards: list):
    new_card = random.choice(cards)
    target_cards.append(new_card)


one_more_game = True
while one_more_game:
    # ask play game
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    is_game_starting = False
    if start_game == 'y':
        is_game_starting = True
    else:
        break

    # game start
    while is_game_starting:
        cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
        user_cards = random.choices(cards, k=2)
        computer_cards = random.choices(cards, k=2)
        cases = {
            "user_over": "You went over. You lose.",
            "com_over": "Oppoent went over. You win.",
            "blackjack": "Win with blackjack!",
            "user_win": "You win.",
            "com_wim": "You lose.",
        }

        # show logo
        print(logo)

        # get cards
        user_score = calculate(user_cards)
        computer_score = calculate(computer_cards)
        is_continue = True
        while is_continue:

            # Show current situation
            print(f"\tYour cards: {user_cards}, current score: {user_score}\n"
                  f"\tComputer's first card: {computer_cards[0]}")

            # blackjack
            if (len(user_cards)== 2) and (11 in user_cards) and (10 in user_cards):
                break

            # Ask user to get another card
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                take_card(cards, user_cards)
                user_score = calculate(user_cards)
                if user_score > 21:
                    break
                continue

            # Ask computer to get another card
            while computer_score < 17:
                take_card(cards, computer_cards)
                computer_score = calculate(computer_cards)
            is_continue = False

        # show final situation
        print(f"\tYour final hand: {user_cards},"
              f" final score: {calculate(user_cards)}\n"
              f"\tComputer's final hand: {computer_cards},"
              f" final score: {calculate(computer_cards)}")

        if (len(user_cards)== 2) and (11 in user_cards) and (10 in user_cards):
            print(cases['blackjack'])
        elif user_score > 21:
            print(cases['user_over'])
        elif computer_score > 21:
            print(cases['com_over'])
        elif user_score > computer_score:
            print(cases['user_win'])
        else:
            print(cases['com_wim'])


        # ask play game or end
        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if start_game == 'n':
            is_game_starting = False
            one_more_game = False
