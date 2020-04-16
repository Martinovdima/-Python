# 4.Определить, какое число в массиве встречается чаще всего.

import timeit
import cProfile
import random


def array_(s):
    SIZE = s
    MIN_ITEM = 0
    MAX_ITEM = 100
    array_ = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    return array_


def max_number(s):
    arr = array_(s)
    number = sorted([(i, arr.count(i)) for i in set(arr)], key=lambda d: d[1])[-1]
    return number[1], number[0]

print(timeit.timeit('max_number(50)', number=100, globals=globals())) # 0.029011796000000006
print(timeit.timeit('max_number(100)', number=100, globals=globals())) # 0.055364128
print(timeit.timeit('max_number(200)', number=100, globals=globals())) # 0.17353843299999996
print(timeit.timeit('max_number(400)', number=100, globals=globals())) # 0.24215614599999996
print(timeit.timeit('max_number(800)', number=100, globals=globals())) # 0.509363451

cProfile.run('max_number(50)')  # 41    0.000    0.000    0.000    0.000 Les_4_task_1_v2.py:18(<lambda>)
                                # 68    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(100)')  # 60    0.000    0.000    0.000    0.000 Les_4_task_1_v2.py:18(<lambda>)
                                 # 129    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(200)')  #  89    0.000    0.000    0.000    0.000 Les_4_task_1_v2.py:18(<lambda>)
                                 #  240    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(400)')  # 99    0.000    0.000    0.000    0.000 Les_4_task_1_v2.py:18(<lambda>)
                                 # 511    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(800)')  # 101    0.000    0.000    0.000    0.000 Les_4_task_1_v2.py:18(<lambda>)
                                 # 1007    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}