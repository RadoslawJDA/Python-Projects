import random
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(cards):
    if sum(cards) == 21:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score2, computer_score):
    if user_score2 == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'You lose'
    elif user_score2 == 0:
        return 'You win'
    elif user_score2 > 21:
        return 'You lost'
    elif computer_score > 21:
        return 'You win'
    elif user_score2 > computer_score:
        return 'You win'
    else:
        return 'You lose'


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Scores
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)
        # Game output
        print(f"Your cards: {user_cards} score: {user_score}")
        print(f"Dealer card: {computer_cards[0]}")

    # user's hit choice
        # if game is over
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_hit = input("Type 'hit' to get another card or 'pass' to pass: ")
            if user_should_hit == 'hit':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # dealer hitting cards
    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    # outcome of a game
    print(f"Your cards: {user_cards} score: {user_score}")
    print(f"Dealer cards: {computer_cards} score: {comp_score}")
    print(compare(user_score, comp_score))


while input("Do you want to play Blackjack Y/N: ") == 'Y':
    os.system('cls')
    play_game()
