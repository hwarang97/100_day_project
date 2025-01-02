import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
select = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if select in {0,1,2}:
    print(choices[select])

    computer = random.randint(0, 2)
    print("Computer chose:" + choices[computer])

    if select == 0:
        if computer == 0:
            print("It's a draw!")
        elif computer == 1:
            print("You lose!")
        else:
            print("You win!")
    elif select == 1:
        if computer == 0:
            print("You win!")
        elif computer == 1:
            print("It's a draw!")
        elif computer == 2:
            print("You lose!")
    elif select == 2:
        if computer == 0:
            print("You lose!")
        elif computer == 1:
            print("You win!")
        elif computer == 2:
            print("It's a draw!")

else:
    print("You typed an invalid number. You lose!")


