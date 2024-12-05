def closest_numbers(numbers, target):
    if not isinstance(numbers, (list, tuple)):
        print("Ошибка: Входные данные должны быть списком или кортежем.")
        return None
    if not all(isinstance(num, (int, float)) for num in numbers):
        print("Ошибка: Входные данные должны содержать только числа.")
        return None
    if not isinstance(target, (int, float)):
        print("Ошибка: Целевое значение должно быть числом.")
        return None
    distances = []
    for number in numbers:
        distance = abs(number - target)
        distances.append((distance, number))
    distances.sort()
    sorted_numbers = [num for dist, num in distances]
    return (target, sorted_numbers)
numbers = [1, 5, 2, 8, 3]
target = 4
result = closest_numbers(numbers, target)
if result:
    target_num, sorted_numbers = result
    print(f"Целевое число: {target_num}")
    print(f"Отсортированные числа: {sorted_numbers}")
numbers2 = [1.5, 2.8, 3.2, 4.7]
target2 = 3
result2 = closest_numbers(numbers2, target2)
if result2:
    target_num2, sorted_numbers2 = result2
    print(f"Целевое число: {target_num2}")
    print(f"Отсортированные числа: {sorted_numbers2}")
numbers3 = [1, "a", 3]
result3 = closest_numbers(numbers3, 2)






numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Чётные числа: {even_numbers}")
words = ["apple", "banana", "cherry", "date"]
upper_words = list(map(lambda word: word.upper(), words))
print(f"Слова в верхнем регистре: {upper_words}")




def get_element_by_index(iterable=None):

    if iterable is None:
        iterable = [1, 2, 3, 4, 5]
    elif not isinstance(iterable, (list, tuple, str)):
        print("Ошибка: iterable должен быть списком, кортежем или строкой.")
        return

    while True:
        try:
            index_input = input("Введите индекс элемента (или 'q' для выхода): ")
            if index_input.lower() == 'q':
                break

            index = int(index_input)
            if 0 <= index < len(iterable):
                element = iterable[index]
                print(f"Элемент по индексу {index}: {element}")
            else:
                print(f"Ошибка: Неверный индекс. Допустимые индексы: от 0 до {len(iterable) - 1}.")
        except ValueError:
            print("Ошибка: Введите целое число или 'q'.")
        except IndexError:
            print(f"Ошибка: Неверный индекс. Допустимые индексы: от 0 до {len(iterable) - 1}.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")




get_element_by_index()

my_string = "Hello"
get_element_by_index(my_string)
get_element_by_index(123)

