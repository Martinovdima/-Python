# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array_ = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_)

min_number = 0
max_number = 0
for i in range(SIZE):
    if array_[i] < array_[min_number]:
        min_number = i
    elif array_[i] > array_[max_number]:
        max_number = i
print(f'Минимальный элемент массива[{min_number}] это {array_[min_number]}, '
      f'максимальный элемент массива [{max_number}] это {array_[max_number]}')
array_[min_number], array_[max_number] = array_[max_number], array_[min_number]
print(array_)
