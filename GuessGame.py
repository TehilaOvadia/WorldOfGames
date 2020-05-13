import random


def generate_number(difficulty):
    return random.randint(1, int(difficulty))


def get_guess_from_user(difficulty):
    return input(f"Enter a number between 1 to {str(difficulty)}:")


def compare_results(difficulty):
    secret_number = generate_number(difficulty)

    if int(get_guess_from_user(difficulty)) == secret_number:
        return True
    else:
        return False


def play(difficulty):
    # print(f"{str(compare_results())} the secret number:  {secret_number}")
    return compare_results(difficulty)
