# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0)
# и 2 нечетные (3 и 5).

def even_number(x):
    y = 0
    for i in x:
        if int(i) % 2 == 0:
            y += 1
    return str(y)


def odd_number(x):
    y = 0
    for i in x:
        if int(i) % 2 != 0:
            y += 1
    return str(y)


a = input(f'Введите число : ')
print(f'{even_number(a)} четных цифры')
print(f'{odd_number(a)} нечетных цифры')
