# from replit import clear
from art import logo

print(logo)

bind_dict = {}


def to_input():
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bind_dict[name] = price


def check_winner():
    bindding_finished = False
    while bindding_finished is False:
        should_continue = input(
            "Are there any other bidders? Type 'yes or 'no'.\n")
        if should_continue == 'yes':
            # clear()
            to_input()
        if should_continue == 'no':
            value_max = 0
            for key in bind_dict:
                value_atual = bind_dict[key]
                if value_atual > value_max:
                    value_max = value_atual
                    winner_name = key

            print(f"The winner is {winner_name} with a bid of {value_max}")
            bindding_finished = True


to_input()
check_winner()
