# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

first_number = input(f'Введите первое шестнадцатиричное число: ')
second_number = input(f'Введите второе шестнадцатиричное число: ')
list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
if len(first_number) > len(second_number):
    first_number, second_number = second_number, first_number
second_number = second_number[::-1]
third_number = deque()
c = -1
k = 0
for i in second_number:
    one = list_of_numbers.index(i)
    two = list_of_numbers.index(first_number[c])
    third_number.appendleft(list_of_numbers[(one + two + k) % 16])
    if (one + two) >= 15:
        k = 1
    else:
        k = 0
    c -= 1
    if c == -len(first_number) - 1:
        break
difference = len(second_number) - len(first_number)
if difference:
    for i in second_number[-difference:]:
        third_number.appendleft(list_of_numbers[(list_of_numbers.index(second_number[-difference]) + k) % 16])
        if list_of_numbers.index(second_number[-difference]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
    third_number.appendleft('1')
print(third_number)
