# calculate average height using for loops
# height inputs
height = input("Input a list of heights e.g. 160 170 130\n").split()
for n in range(0, len(height)):
    height[n] = int(height[n])
print(f"List of pasted heights:{height}")

# sum of heights
height_sum = 0
for x in height:
    height_sum = height_sum + x
print(f"sum of heights: {height_sum}")

# length of heights
length_count = 0
for len_height in height:
    length_count += 1
print(f"length of list: {length_count}")

# average height
average_height = height_sum/length_count
print(f"Average height is: {average_height}")
