# You are going to write a program that calculates the average student height from a List of heights.
# you are not allowed to use len() and sum() in the logic 

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

count = 0
total_height = 0

for student in student_heights:
    total_height += student
    count += 1

average_height = float(total_height / count)
print(f"The average height is {average_height}")