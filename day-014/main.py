import random
from art import logo, vs
from game_data import data
import os

# CODE OUTLINE:


def select_peaple(type_person: str, length_data_list: int) -> int:
    index_a = random.randint(0, length_data_list)
    if type_person == 'A':
        return index_a
    elif type_person == 'B':
        index_b = index_a
        while index_b == index_a:
            index_a = random.randint(0, length_data_list)
        return index_b


def show_a_vs_b(dict_a, dict_b):
    if score == 0:
        print(logo)
    else:
        print(f"You're right! Current score: {score}")
        print(logo)

    print(
        f'Compare A: {dict_a["name"]}, a {dict_a["description"]}, from {dict_a["country"]}.')
    print(vs)
    print(
        f'Compare B: {dict_b["name"]}, a {dict_b["description"]}, from {dict_b["country"]}.')


def return_answer(dict_a, dict_b):
    if dict_a["follower_count"] > dict_b["follower_count"]:
        answer = 'A'
    else:
        answer = 'B'
    return answer


def comparate_guess_answer():
    if guess == answer:
        return True
    else:
        return False


end_game = False
score = 0
length_data_list = (len(data) - 1)
while end_game == False:

    index_person_a = select_peaple('A', length_data_list)
    index_person_b = select_peaple('B', length_data_list)

    show_a_vs_b(data[index_person_a], data[index_person_b])

    guess = input("Who has more followers? Type 'A' or 'B': ")

    answer = return_answer(data[index_person_a], data[index_person_b])

    comparate = comparate_guess_answer()
    if comparate is True:
        score += 1
        os.system('cls')  # Turn 'clear' for linux
    else:
        os.system('cls')  # Turn 'clear' for linux
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        end_game = True
