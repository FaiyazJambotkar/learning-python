print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = str.lower(name1)
name2 = str.lower(name2)

names = name1 + name2

true_count = 0
love_count = 0

true_count = names.count('t')
true_count += names.count('r')
true_count += names.count('u')
true_count += names.count('e')

love_count = names.count('l')
love_count += names.count('o')
love_count += names.count('v')
love_count += names.count('e')

score = str(true_count) + str(love_count)

int_score = int(score)
if int_score <= 50:
    print(f"Your score is {score}, you are alright together.")
elif int_score > 50 and int_score < 100:
    print(f"Your score is {score}")
else:
    print(f"Your score is {score}, you go together like coke and mentos.")