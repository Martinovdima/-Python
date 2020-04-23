# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.
import sys
from collections import defaultdict


def show(x):
    summary = 0
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    summary += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                summary += sys.getsizeof(key)
                show(value)
                summary += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)
                summary += sys.getsizeof(item)
    return f'type={type(summary)}, size={sys.getsizeof(summary)}, obj={summary}\n'\
           f'Объем занятой памяти {summary + sys.getsizeof(summary)} байта.'\



numbers = defaultdict(int)
for k in range(2, 10):
    n = 0
    for v in range(2, 100):
        if v % k == 0:
            n += 1
    numbers[k] += n
for k, v in numbers.items():
    print(f'Числу {k} кратны {v} чисел из диапазона от 2 до 99')

print(show(numbers))

# Объем занятой памяти 852 байта


