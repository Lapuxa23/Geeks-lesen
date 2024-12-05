data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)
numbers.remove(6.13)
letters.append(numbers.pop(numbers.index(True)))
numbers.insert(numbers.index(3) + 1, 2)
numbers.sort()
letters.reverse()
letters[-2] = letters[-2].lower()
numbers = [x**2 for x in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(f"Кортеж letters: {letters}")
print(f"Кортеж numbers: {numbers}")
