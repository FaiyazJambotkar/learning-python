#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

bill   = float(input("What was the total bill?\n"))
tip    = float(input("What percentage tip would you like to give? 10, 12 or 15? \n"))
people = int(input("How many people to split the bill?\n"))

total_tip    = (bill * tip) / 100 
total_bill   = bill + total_tip
per_person   = total_bill / people
rounded_bill = round(per_person,2)

rounded_bill ="{:0.2f}".format(per_person)

print(f"\nEach person should pay {rounded_bill}")