# Creating a Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easier Version

password = ""
for chars in range(1, nr_letters + 1):
    password += random.choice(letters)

for nums in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symbs in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(f"Simple password is: {password}")


# Difficult version

password = []
for chars in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for nums in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

for symbs in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

password_str = ""
for values in password:
    password_str += values

print(f"Secure pasword is: {password_str}")
