def calculate():


    while True:
        print("\nДоступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("q. Выход")

        choice = input("Выберите операцию (1/2/3/4/q): ")

        if choice.lower() == 'q':
            print("uff home.")
            break

        try:
            num1 = float(input(" первое число: "))
            num2 = float(input(" второе число: "))

            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    print("0//!")
                    continue
                result = num1 / num2
            print("Результат:", result)

        except ValueError:
            print("loh, введите числа.")


if __name__ == "__main__":
    calculate()
