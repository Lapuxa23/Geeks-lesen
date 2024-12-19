def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for t in range(0, n - i - 1):
            if list[t] >list[t + 1]:
                list[t], list[t + 1] =list[t + 1], list[t]
    return list

