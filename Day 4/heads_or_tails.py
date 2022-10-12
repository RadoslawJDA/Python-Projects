# Guess heads or tails
import random

user_choice = input("Heads or Tails? \n")
random_integer = random.randint(1, 2)

if random_integer == 1:
    random_choice = "Heads"
else:
    random_choice = "Tails"
print(f"Coin showed {random_choice}\n")

if user_choice == random_choice:
    print("You guessed it")
else:
    print("You didn't guessed it")
