import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"random word: {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")


end_of_game = False
mistakes = 2

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    position = 0

    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
        position += 1
    if guess not in chosen_word:
        mistakes -= 1

    print(f"password: {display}")
    print(f"mistakes left : {mistakes}")

# ending
    if "_" not in display:
        end_of_game = True
        print("You win!")

    if mistakes == 2:
        end_of_game = True
        print("you hanged the guy, you lost!")





