# Add ticket based on age and check if photo need to be taken

age = 0
height = int(input("What is your height in cm: "))

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("\nWhat is your age?\n"))
    if age <= 12:
        bill = 5
        print(f"Your ticket charges are: {bill}")
    elif age < 18:
        bill = 7
        print(f"Your ticket charges are: {bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print("It's on us")
    
    else:
        bill = 12
        print(f"Your ticket charges are: {bill}")

    photo = str(input("\nDo you want a photo taken? y or n?\n"))
    if photo == 'y':
        bill += 3

    print(f"\nYour total bill = {bill}")

else:
    print("\nYou need to grow taller to ride the rollercoaster!")
