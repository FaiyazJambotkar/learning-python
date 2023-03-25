# write a program that calculates the highest score from a List of scores.
# you are not allowed to use the max or min functions.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if highest_score < score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")