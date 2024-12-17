import random


def game_logic(balance, min_number, max_number, attempts):
    print(f"Ваш баланс: {balance}")

    while attempts > 0 and balance > 0:
        print(f"Осталось попыток: {attempts}")
        guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
        number_to_guess = random.randint(min_number, max_number)

        if guess == number_to_guess:
            print(f"Поздравляем! Вы угадали число {number_to_guess}. Ставка удвоена!")
            balance *= 2
        else:
            print(f"Неправильно! Загаданное число было {number_to_guess}. Вы теряете ставку.")
            balance -= 1

        print(f"Текущий баланс: {balance}")
        attempts -= 1

    if balance <= 0:
        print("Ваш баланс закончился. Игра окончена!")
    else:
        print("Поздравляем! Игра завершена.")