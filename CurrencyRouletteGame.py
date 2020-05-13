from currency_converter import CurrencyConverter
import random

c = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')
top_money = int(c.convert(100, 'USD', 'ILS'))
bottom_money = int(c.convert(1, 'USD', 'ILS'))
t = int(c.convert(random.randint(1, 100), 'USD', 'ILS'))


def get_money_interval(d):
    amount_range = (t - (5 - d), t + (5 - d))
    return amount_range


def get_guess_from_user():
    return input(f"Enter a guess of value to a given amount between {bottom_money} - {top_money}: ")


def compare_results(difficulty):
    money_interval = get_money_interval(difficulty)
    user_guess = int(get_guess_from_user())

    if money_interval[0] <= user_guess <= money_interval[1]:
        return True
    else:
        return False


def play(difficulty):
    return compare_results(difficulty)
