from logic import game_logic
from decouple import config


def load_config():
    min_number = config('min_number', cast=int)
    max_number = config('max_number', cast=int)
    attempts = config('attempts', cast=int)
    starting_balance = config('starting_balance', cast=int)
    return min_number, max_number, attempts, starting_balance


def main():
    min_number, max_number, attempts, starting_balance = load_config()

    print("Добро пожаловать в игру 'Угадай число!'")
    game_logic(starting_balance, min_number, max_number, attempts)


if __name__== "__main__":
    main()