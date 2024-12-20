def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
def binary_search(element, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == element:
            print(f"Элемент {element} найден в списке.")
            return True
        elif sorted_list[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Элемент {element} не найден в списке.")
    return False
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
element_to_search = 22
binary_search(element_to_search, sorted_list)
element_to_search = 100
binary_search(element_to_search, sorted_list)
