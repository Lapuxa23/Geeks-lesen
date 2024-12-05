def nearest_number(numbers, target=0):
    if not numbers: return None
    return min(numbers, key=lambda num: abs(num - target))
print(nearest_number([1, 2, 3], 5))
print(nearest_number([1.5, 2.7, 3.2, 10.1], 3))
print(nearest_number([-10, 5, 15, 20], 0))
print(nearest_number([], 5))

print(nearest_number("not a list", 5))

