import random

def guess_number():


    low = 1
    high = 100
    attempts = []
    count = 0

    while True:
        guess = (low + high) // 2
        count += 1
        attempts.append(guess)

        print(f"Моя попытка №{count}: {guess}")

        answer = input("Число больше, меньше или равно (больше/меньше/равно): ").lower()

        if answer == "равно":
            print(f"Я угадал за {count} попыток!")
            with open("results.txt", "w") as f:
                f.write(f"Количество попыток: {count}\n")
                f.write(f"Список попыток: {attempts}\n")
                f.write(f"Загаданное число: {guess}\n")
            break
        elif answer == "больше":
            low = guess + 1
        elif answer == "меньше":
            high = guess - 1
        else:
            print("Неверный ввод. Пожалуйста, введите 'больше', 'меньше' или 'равно'.")

if __name__ == "__main__":
    guess_number()
