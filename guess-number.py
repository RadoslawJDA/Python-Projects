import random


def live_check(live_count):
    if live_count == 0:
        finish_game = True
        return finish_game
    else:
        finish_game = False
        return finish_game


def game(lives):
    finish_game = False
    print("Guess random number from 1 to 10")
    random_int = random.randint(1, 10)
    print(lives)
    while not finish_game or lives == 0:

        guess = int(input("Your guess: "))
        live_check(lives)
        if guess > random_int:
            print("Lower")
            lives -= 1
            print(f'{lives} guesses left')
        elif guess < random_int:
            print("Higher")
            lives -= 1
            print(f'{lives} guesses left')
        elif guess == random_int:
            print(f"GoodJob you guessed it random number is: {random_int}")
            finish_game = True

        if lives == 0:
            print('You lost')
            return


def difficulty_set():
    difficulty = input("Choose difficulty: 'Normal' or 'Hard': ").capitalize()

    if difficulty == 'Normal':
        game(10)
    elif difficulty == 'Hard':
        game(5)
    else:
        print("Choose between Normal or Hard: ")
        difficulty_set()


difficulty_set()
