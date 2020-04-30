# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# a, p, pa, ap, apa, pap
# 6
# func("sova")
# 9


def subs(_str):
    sub = set()
    for i in range(len(a)):
        for j in range(len(a) - 1 if i == 0 else len(a), i, -1):
            sub.add(hash(a[i:j]))
    return len(sub)


a = input(f'Введите строку: ')
print(f'Количество различных подстрок в этой строке: {subs(a)}')
