import random

rock = "rock"
paper = "paper"
scissors = "scissors"
choices = [rock, paper, scissors]

rand_int = random.randint(0, 2)
user_input = int(input("Choose 0-Rock 1-Paper 2-Scissors\n"))

if user_input > 2 or user_input < 0:
    print("You typed and invalid number, (0 - 2)")
else:
    user_choice = choices[user_input]
    rand_choice = choices[rand_int]

    print(f"you chose: {user_choice}")
    print(f"computer chose: {rand_choice}")

    if user_input == 0 and rand_int == 2:
        print("you win!")
    elif user_input == 2 and rand_int == 0:
        print("you lose!")
    elif user_input > rand_int:
        print("you win!")
    elif user_input == rand_int:
        print("DRAW!")
    else:
        print("you lose!")
