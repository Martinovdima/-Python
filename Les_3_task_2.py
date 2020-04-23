# 2.Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array_ = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

array_idx = []
for i in range(SIZE):
    if array_[i] % 2 == 0:
        array_idx.append(i)
print(f'Индексы {array_idx} четных элементов в массиве {array_}.')

