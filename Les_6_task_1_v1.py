# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из
# них кратны каждому из чисел в диапазоне от 2 до 9.
import sys


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
    return f'type={type(summary)}, size={sys.getsizeof(summary)}, obj={summary}\n' \
           f'Объем занятой памяти {summary + sys.getsizeof(summary)} байта.' \



numbers = [0] * 8
for i in range(2, 100):
    for k in range(2, 10):
        if i % k == 0:
            numbers[k - 2] += 1
i = 0
while i < len(numbers):
    print(f'Числу {i + 2} кратны {numbers[i]} чисел из диапазона от 2 до 99')
    i += 1

print(show(numbers), show(i), show(k), sep='\n')

# Объем занятой памяти 492 байта