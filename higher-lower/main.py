from game_data import data
import random
import os


def get_choice():

    first_choice = random.choice(data)
    second_choice = random.choice(data)

    first_followers = first_choice['follower_count']
    second_followers = second_choice['follower_count']

    # answers list
    first_choice_index = data.index(first_choice)
    second_choice_index = data.index(second_choice)
    answers = [first_choice_index, second_choice_index]

    print(f"{first_choice['description']} {first_choice['name']} from "
          f"{first_choice['country']} with {first_choice['follower_count']} followers")
    print('OR')
    print(f"{second_choice['description']} {second_choice['name']} from "
          f"{second_choice['country']} with {second_choice['follower_count']} followers")

    return answers, first_followers, second_followers, second_choice_index


def another_choice(question, answers2):
    first_choice = data[question]
    second_choice = random.choice(data)

    index = data.index(second_choice)
    while index in answers2:
        second_choice = random.choice(data)
        index = data.index(second_choice)

    answers.append(index)

    first_followers = first_choice['follower_count']
    second_followers = second_choice['follower_count']

    print(f"{first_choice['description']} {first_choice['name']} from "
          f"{first_choice['country']} with {first_choice['follower_count']} followers")
    print('OR')
    print(f"{second_choice['description']} {second_choice['name']} from "
          f"{second_choice['country']} with {second_choice['follower_count']} followers")

    return first_followers, second_followers, answers


# indexes of used dictionaries, followers
answers, first_followers, second_followers, second_choice_index = get_choice()

# main
bad_answer = 0
good_answer = 0
while bad_answer == 0:

    usr_input = input("Higher or lower H/L: ").upper()

    print(first_followers, second_followers)
    if usr_input == 'H' and first_followers < second_followers:
        good_answer += 1
        os.system('cls')
        print("Let's goo")
        first_followers, second_followers, answers = another_choice(second_choice_index, answers)

    elif usr_input == 'L' and first_followers > second_followers:
        good_answer += 1
        os.system('cls')
        print("Let's goo")
        first_followers, second_followers, answers = another_choice(second_choice_index, answers)
    else:
        bad_answer = 1
        print(f'You lost, score: {good_answer}')
        break


