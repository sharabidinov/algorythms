"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import Counter

QUARTER = 4
company_info = Counter()
company_amount = int(input('Введите количество компаний: '))

while company_amount != 0:
    company_name = input(f'Введите наименование компании: ')
    company_info[company_name] = []
    for i in range(QUARTER):
        quarter_input = int(input(f'Введите прибыль за {i + 1} квартал: '))
        profit = company_info[company_name]
        profit.append(quarter_input)
    company_amount -= 1


def avg_profit(data: Counter):
    avg_divider = len(tuple(data.values()))
    total_sum = 0

    for key in data:
        total_sum += sum(data[key])

    avg = total_sum / avg_divider
    return avg


profitable_companies = []
unprofitable_companies = []

for key in company_info:
    if sum(company_info[key]) > avg_profit(company_info):
        profitable_companies.append(key)
    else:
        unprofitable_companies.append(key)

print('Компании чья прибыль выше среднего:')
print(*profitable_companies, sep='\n')
print('Компании чья прибыль ниже среднего:')
print(*unprofitable_companies, sep='\n')
