"""
The Rock_paper_scissors game is played when players deliver hand signals that will represent the
elements of the game; rock, paper and scissors. The outcome of the game is determined by 3 simple rules:
ROCK WINS AGAINST SCISSORS
SCISSORS WINS AGAINST PAPER
PAPER WINS AGAINST ROCK

rock > scissors = win
scissors > paper = win
paper > rock = win

"""

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
game = [rock, paper, scissors]
user_choice = int(input("What do you choose? 0 for rock, 1 for paper and 2 for scissors?\n"))
if user_choice >= 3 or user_choice < 0:
    print("The number is out of range, You Lose!!!!")
else:
    print(f"You chose {game[user_choice]}")

    computer_choice = random.randint(0, 2)
    #computer_choice = game[computer_choice]
    print(f"Computer chose {game[computer_choice]}")

    if user_choice == computer_choice:
        print("You have a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif user_choice > computer_choice:
        print("You win")
    else:
        print("You lose")




