# Creating a game of rock paper and scissors

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

img = [rock, paper, scissors]
# print(f"{rock}\nrock\n{paper}\npaper\n{scissors}\nscissors\n")

user_choice = int(input("What do you choose: press 1 for rock, 2 for paper or 3 for scissors?\n"))
computer_choice = int(random.randint(0,2))

print("\nYou chose: ")
print(img[user_choice - 1])

print("\nComputer chose: ")
print(img[computer_choice])

# rock - 0
# paper - 1
# scissors - 2

print("\n")
if (computer_choice == (user_choice - 1)):
    print("It's a draw.")
elif ((user_choice == 1) and (computer_choice == 0)):
    print("You Win!")
elif ((user_choice == 0) and (computer_choice == 2)):
    print("You Win!")
elif ((user_choice == 2) and (computer_choice == 1)):
    print("You Win!")
else:
    print("You lose.")

