# write a program that calculates the sum of all the even numbers from 1 to 100.
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

sum = 0
for number in range(2, 101, 2):
    sum += number

print(sum)

sum2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum2 += number

print(sum2)