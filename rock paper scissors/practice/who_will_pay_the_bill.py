import random

name_input = input("Input the names separated by comma e.g. Rad, Dar \n")
names = name_input.split(", ")

print(random.choice(names) + " will pay for the bill.")
