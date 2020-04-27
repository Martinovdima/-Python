# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
START = 0


def median(arr, l):
    left = []
    right = []
    med = arr[l]
    for i in arr:
        if i <= med:
            left.append(i)
        else:
            right.append(i)
    if len(left) == (SIZE + 1):
        return f'Медианой является число: {max(left)}'
    elif len(right) == (SIZE + 1):
        return f'Медианой является число: {min(right)}'
    else:
        return median(arr, l + 1)


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range((SIZE * 2) + 1)]
print(array)
print(median(array, START))
print(sorted(array))
