from collections import Counter
companies = {}
company = int(input('Введите количество Ваших предприятий: '))
profit = 0
for i in range(company):
    name = input('Название предприятия: ')
    profit_1 = int(input('Прибыль за 1 квартал: '))
    profit_2 = int(input('Прибыль за 2 квартал: '))
    profit_3 = int(input('Прибыль за 3 квартал: '))
    profit_4 = int(input('Прибыль за 4 квартал: '))
    profit = profit_1 + profit_2 + profit_3 + profit_4
    companies[name] = [profit]
count = Counter(companies)

total_value = sum(map(sum, count.values()))
average = total_value / company

print(f'средняя прибыль за год для всех предприятий {average}')
print(f'прибыль за 4 квартал {count}')






