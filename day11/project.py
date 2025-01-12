from art import logo
import random


# Constant Declaration
CARDS = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
CASES = {
            "draw": "Draw.",
            "user_over": "You went over. You lose.",
            "com_over": "Opponent went over. You win.",
            "user_blackjack": "Win with blackjack!",
            "computer_blackjack": "Lose, opponent has Blackjack.",
            "user_win": "You win.",
            "com_wim": "You lose.",
        }


def calculate_sum(cards: list) -> int:
    """Take a list of cards and return the score calculated from the cards

    Args:
        cards (list): containing cards

    Returns:
        int: sum of cards
        - 0: blackjack
        - Otherwise: the score calculated from cards
    """
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score -= 10

    return score

def take_card(cards: list, target_cards: list):
    """Take a card"""
    new_card = random.choice(cards)
    target_cards.append(new_card)

def print_game_status(user_cards: list, user_score: int, computer_cards: list):
    """Print current each score and cards of user and computer"""
    print(f"\tYour cards: {user_cards}, current score: {user_score}\n"
          f"\tComputer's first card: {computer_cards[0]}")

def print_final_situation(user_cards, computer_cards):
    """Print final each score and cards of user and computer"""
    print(f"\tYour final hand: {user_cards},"
          f" final score: {calculate_sum(user_cards)}\n"
          f"\tComputer's final hand: {computer_cards},"
          f" final score: {calculate_sum(computer_cards)}")

def compare(user_score: int, computer_score: int) -> str:
    """Compare two scores and return result

    Args:
        user_score (int): score of user
        computer_score (int): score of computer

    Returns:
        str: Game result e.g "You lose."
    """
    if user_score == computer_score:
        return CASES['Draw']
    elif user_score == 0:
        return CASES['user_blackjack']
    elif computer_score == 0:
        return CASES['computer_blackjack']
    elif user_score > 21:
        return CASES['user_over']
    elif computer_score > 21:
        return CASES['com_over']
    elif user_score > computer_score:
        return CASES['user_win']
    else:
        return CASES['com_wim']

def play_blackjack():
    # initialize
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(random.choice(CARDS))
        computer_cards.append(random.choice(CARDS))

    # show logo
    print(logo)

    is_game_over = False
    while not is_game_over:

        # Calculate score
        user_score = calculate_sum(user_cards)
        computer_score = calculate_sum(computer_cards)

        # Show current situation
        print_game_status(user_cards, user_score, computer_cards)

        # Check game over
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user to get another card
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                take_card(CARDS, user_cards)
            elif get_another_card == 'n':
                is_game_over = True
                
        # Ask computer to get another card
        while computer_score != 0 and computer_score < 17:
            take_card(CARDS, computer_cards)

    # show final situation
    print_final_situation(user_cards, computer_cards)

    # show result
    print(compare(user_score, computer_score))


def main():
    while True:
        # ask play game
        is_start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if is_start_game == 'y':
            play_blackjack()
        elif is_start_game == 'n':
            break


if __name__ == "__main__":
    main()
