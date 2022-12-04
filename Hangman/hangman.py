import random

import hangman_words
import hangman_art

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(f"Password: {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")

# variables
end_of_game = False
lives = 5
hangman_art_position = 5

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    position = 0

    if guess in display:
        print(f"you've already guessed that letter {guess}")

    for letter in chosen_word:
        if letter == guess:
            display[position] = letter
        position += 1

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        print(hangman_art.stages[hangman_art_position])
        hangman_art_position -= 1
        if lives == 0:
            end_of_game = True
            print("you hanged the guy, you lost!")

    print(f"password: {display}")
    print(f"mistakes left : {lives}")

# ending
    if "_" not in display:
        end_of_game = True
        print("You win!")


