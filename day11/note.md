## Indicate cards and cases as constant variable
Constant variables are typically located below import statements in Python. According to PEP 8 (Python Style Guide), it is recommended to place import statements at the top of the source code.
To improve code readability and clearly indicate the use of constant variables, constants are positioned directly below the import statements.   
__Before__
```python
cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
cases = {
    "user_over": "You went over. You lose.",
    "com_over": "Oppoent went over. You win.",
    "blackjack": "Win with blackjack!",
    "user_win": "You win.",
    "com_wim": "You lose.",
}
```
__After__
```python
from art import logo
import random


CARDS = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
CASES = {
    "user_over": "You went over. You lose.",
    "com_over": "Oppoent went over. You win.",
    "blackjack": "Win with blackjack!",
    "user_win": "You win.",
    "com_wim": "You lose.",
}
```

## Use status variable instead of continue or break keyword for better readability
Using the keywords break and continue can reduce the readability of logic. Instead, using a status variable often improves clarity and makes the flow of the code easier to understand. 
The break and continue keywords are best suited for short and simple code snippets.   
__Before__
```python
# Ask user to get another card
get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
if get_another_card == 'y':
    take_card(CARDS, user_cards)
    user_score = calculate(user_cards)
    if user_score > 21:
        break
    continue
```

__After__
```python
# Ask user to get another card
get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
if get_another_card == 'y':
    take_card(CARDS, user_cards)
    user_score = calculate(user_cards)
    if user_score > 21:
        is_continue = False # Use status variable
    continue
```

## When using nested while loops, it is better for readability to separate them into individual functions.
__Before__
```python
one_more_game = True
while one_more_game:
    ...
    # game start
    while is_game_starting:
        ...

```

__After__
```python

```
