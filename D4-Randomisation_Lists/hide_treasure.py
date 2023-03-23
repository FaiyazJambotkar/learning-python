# You are going to write a program that will mark a spot with an X.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

col_num = int(position[0])
row_num = int(position[1])

map[row_num - 1][col_num - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")