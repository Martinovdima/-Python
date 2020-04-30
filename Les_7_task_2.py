# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50


def merge(left, right):
    result = []
    i, k = 0, 0
    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[k])
            k += 1
    result += left[i:]
    result += right[k:]
    return result


def sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left = sort(arr[:middle])
    right = sort(arr[middle:])
    return merge(left, right)


array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print(sort(array))
