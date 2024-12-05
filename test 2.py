def calculator(num1: float, operator: str, num2: float) -> float:
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                return " на ноль недопустимо!"
            else:
                return num1 / num2
        elif operator == '//':
            if num2 == 0:
                return " ноль недопустимо!"
            else:
                return num1 // num2
        elif operator == '%':
            if num2 == 0:
                return "Деление на ноль недопустимо!"
            else:
                return num1 % num2
        elif operator == '*':
            return num1 * num2
        else:
            return "errror!"
    except ValueError:
        return "number ."
    except Exception as e:
        return f"Произошла ошибка: {e}"

print(calculator(10, "+", 5))
print(calculator(10, "-", 5))
print(calculator(10, "*", 5))
print(calculator(10, "/", 5))
print(calculator(10, "/", 0))
print(calculator(10, "//", 5))
print(calculator(10, "%", 3))
print(calculator(2, "*", 3))
print(calculator(10, "abc", 5))
print(calculator("hello", "+", 5))
#Это конечно  странно но мой меняет давал такое задание.




