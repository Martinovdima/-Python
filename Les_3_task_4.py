# 4.Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array_ = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_)

num = array_[0]
count = 1
for i in range(SIZE - 1):
    n = 1
    for k in range(i + 1, SIZE):
        if array_[i] == array_[k]:
            n += 1
    if n > count:
        count = n
        num = array_[i]

if count > 1:
    print(f'В массиве {count} раза повторяется число {num}.')
else:
    print(f'Нет повторяющихся элементов в массиве.')
