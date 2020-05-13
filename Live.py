import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'


def load_game():
    title = 'Please choose a game to play:'
    rul_1 = '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'
    rul_2 = '2. Guess Game - guess a number and see if you chose like the computer'
    rul_3 = '3. Currency Roulette - try and guess the value of a random amount of USD in ILS'

    choice = int(input(f'{title} \n\t{rul_1}\n\t{rul_2}\n\t{rul_3}\n'))
    is_not_choice = True

    while is_not_choice:
        if int(choice) > 3 or int(choice) < 1:
            choice = int(input(f'Please enter the game number (between 1 to 3)'
                           f'\n{title} \n\t{rul_1}\n\t{rul_2}\n\t{rul_3}\n'))
        else:
            is_not_choice = False

    difficulty = int(input('Please choose game difficulty from 1 to 5:\n'))
    is_not_difficulty = True

    while is_not_difficulty:
        if int(difficulty) > 5 or int(difficulty) < 1:
            difficulty = int(input('Please choose game difficulty from 1 to 5:\n'))
        else:
            is_not_difficulty = False

    if choice == 1:
        print(MemoryGame.play(difficulty))
    elif choice == 2:
        print(GuessGame.play(difficulty))
    elif choice == 3:
        print(CurrencyRouletteGame.play(difficulty))
