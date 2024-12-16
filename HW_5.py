import random

min_number = 1
max_number = 10
max_attempts = 3
initial_capital = 10


def play_game():
    secret_number = random.randint(min_number, max_number)
    capital = initial_capital
    attempts_left = max_attempts

    print(f"Угадайте число от {min_number} до {max_number} за {max_attempts} попыток!")

    for attempt in range(max_attempts):
        print(f"\nПопытка {attempt+1}/{max_attempts}, капитал: {capital}")
        try:
            bet = int(input("Введите ставку: "))
            guess = int(input("Введите число: "))
            if guess == secret_number:
                capital += bet * 2
                print("Вы угадали! Выиграли:", bet * 2)
                return
            else:
                capital -= bet
                print("Не угадали.")
                if capital <= 0:
                    print("Игра окончена. Недостаточно средств.")
                    return
        except ValueError:
            print("Ошибка ввода. Введите целое число.")

    print(f"Вы проиграли. Загаданное число: {secret_number}")


if __name__ == "__main__":
    play_game()
