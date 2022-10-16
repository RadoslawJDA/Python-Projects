# max number using for loop

number = input("Input a list of numbers e.g. 1 2 3\n").split()
for n in range(0, len(number)):
    number[n] = int(number[n])
print(f"List of pasted numbers:{number}")

max_value = 0
for value in number:
    if value > max_value:
        max_value = value

print(f"max value is: {max_value}")