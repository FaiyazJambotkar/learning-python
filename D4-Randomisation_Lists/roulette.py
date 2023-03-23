# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

no_of_people = len(names)
choice = random.randint(0, no_of_people - 1)

print(f"{names[choice]} is going to buy the meal today!")