
row0 = ["0 ", "1 ", "2 "]
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
island = [row1, row2, row3]
print(f"{row0}\n{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (column and row e.g. 11)\n")

horizontal = int(position[0])
vertical = int(position[1])

island[horizontal][vertical] = "x"

print(f"{row0}\n{row1}\n{row2}\n{row3}")
