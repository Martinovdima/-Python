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
    a_sort = sorted(arr)
    elem = None
    n = 1
    count = 1
    for i in range(s - 2):
        if a_sort[i] == a_sort[i + 1]:
            count += 1
            if n < count:
                elem = a_sort[i]
                n = count
        else:
            count = 1
    if n < 2:
        return 0
    else:
        return elem


print(timeit.timeit('max_number(50)', number=100, globals=globals()))  # 0.016876434000000003
print(timeit.timeit('max_number(100)', number=100, globals=globals()))  # 0.034059866
print(timeit.timeit('max_number(200)', number=100, globals=globals()))  # 0.06788725400000001
print(timeit.timeit('max_number(400)', number=100, globals=globals()))  # 0.13917469200000002
print(timeit.timeit('max_number(800)', number=100, globals=globals()))  # 0.2833827300000001

cProfile.run('max_number(50)')  # 1    0.000    0.000    0.000    0.000 Les_4_task_1_v3.py:16(max_number)
                                # 61    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(100)')  # 1    0.000    0.000    0.000    0.000 Les_4_task_1_v3.py:16(max_number)
                                 # 124    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(200)')  # 1    0.000    0.000    0.001    0.001 Les_4_task_1_v3.py:16(max_number)
                                 # 281    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(400)')  # 1    0.000    0.000    0.002    0.002 Les_4_task_1_v3.py:16(max_number)
                                 # 510    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(800)')  # 1    0.000    0.000    0.004    0.004 Les_4_task_1_v3.py:16(max_number)
                                 # 1014    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}