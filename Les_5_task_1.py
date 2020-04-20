# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import defaultdict

company_d = defaultdict(int)
company = []
company_count = int(input('Введите количество предприятий: '))
for _ in range(company_count):
    company.append(input(f'Введите название предприятия № {_ + 1}: '))
    period = 4
    cash_pool = 0
    for i in range(period):
        cash_pool += int(input(f'Введите сумму прибыли за {i + 1} квартал: '))
    company_d[company[_]] += cash_pool
cash_cp = ((sum(company_d.values())) / company_count)
for k, v in company_d.items():
    if v > cash_cp:
        print(f' У предприятия {k} прибыль {v} выше среднего (среднее {cash_cp}).')
    if v == cash_cp:
        print(f' У предприятия {k} средняя прибыль {v}.')
    if v < cash_cp:
        print(f' У предприятия {k} прибыль {v} ниже среднего (среднее {cash_cp}).')

