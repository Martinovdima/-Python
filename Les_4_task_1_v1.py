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
    num = arr[0]
    count = 1
    for i in range(s - 1):
        n = 1
        for k in range(i + 1, s):
            if arr[i] == arr[k]:
                n += 1
        if n > count:
            count = n
            num = arr[i]

    if count > 1:
        return num
    else:
        return 0


print(timeit.timeit('max_number(50)', number=100, globals=globals())) # 0.038970948
print(timeit.timeit('max_number(100)', number=100, globals=globals())) # 0.125175476
print(timeit.timeit('max_number(200)', number=100, globals=globals())) # 0.403568143
print(timeit.timeit('max_number(400)', number=100, globals=globals())) # 1.5599985539999999
print(timeit.timeit('max_number(800)', number=100, globals=globals())) # 7.132701398

cProfile.run('max_number(50)')  #  1    0.000    0.000    0.000    0.000 Les_4_task_1_v1.py:15(max_number)
                                #  72    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(100)')  # 1    0.001    0.001    0.001    0.001 Les_4_task_1_v1.py:15(max_number)
                                 # 128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(200)')  # 1    0.003    0.003    0.004    0.004 Les_4_task_1_v1.py:15(max_number)
                                 #  257    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(400)')  # 1    0.012    0.012    0.013    0.013 Les_4_task_1_v1.py:15(max_number)
                                 # 503    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('max_number(800)')  # 1    0.050    0.050    0.053    0.053 Les_4_task_1_v1.py:15(max_number)
                                 # 1028    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}