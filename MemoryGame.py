import random


def generate_sequence(difficulty):
    rand_numbers = []

    for i in range(int(difficulty)):
        rand_numbers.append(random.randint(1, 101))

    return rand_numbers


def get_list_from_user(difficulty):
    user_numbers = []
    num_txt = "numbers"

    if difficulty == 1:
        num_txt = "number"

    print(f"Enter {difficulty} {num_txt} between 1-101")
    for i in range(int(difficulty)):
        user_numbers.append(int(input()))

    return user_numbers


def is_list_equal(difficulty):
    rand_numbers = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)

    rand_numbers.sort()
    user_numbers.sort()

    if rand_numbers == user_numbers:
        return True
    else:
        return False


def play(difficulty):
    return is_list_equal(difficulty)
