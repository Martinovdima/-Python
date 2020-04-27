import random
from collections import Counter

SIZE = 10
MIN_ITEM = 5
MAX_ITEM = 6
START = 0
IDX = 1


def median(arr, l, idx):
    if l < ((SIZE * 2) + 1):
        left = []
        right = []
        med = arr[l]
        for i in arr:
            if i <= med:
                left.append(i)
            else:
                right.append(i)
        if len(left) == (SIZE + idx):
            return f'Медианой является число: {max(left)}'
        elif len(right) == (SIZE + idx):
            return f'Медианой является число: {min(right)}'
        else:
            return median(arr, l + 1, idx)
    else:
        idx += 1
        return median(arr, 0, idx)


def unique(arr, l, idx):
    uniq = 0
    for _ in set(arr):
        uniq += 1
    if uniq <= 2:
        array = Counter(arr)
        for k, v in array.items():
            if v == SIZE or v == SIZE + 1:
                return median(arr, l, idx)
            else:
                return (sum(set(arr)) / 2)
    else:
        return median(arr, l, idx)


array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range((SIZE * 2) + 1)]
print(array)
print(unique(array, START, IDX))
print(sorted(array))
