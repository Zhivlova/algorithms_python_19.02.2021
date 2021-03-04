"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 99):
        if f % n == 0:
            result[n].append(f)
    print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')


# второй вариант
import random

my_list = [random.randint(2, 99) for _ in range(2,99)]
print(my_list)

new_list = [el for el in my_list if el % 2 == 0]
print(f'{new_list} кратны 2 ')
new_list_3 = [el for el in my_list if el % 3 == 0]
print(f'{new_list_3} кратны 3 ')
new_list_4 = [el for el in my_list if el % 4 == 0]
print(f'{new_list_4} кратны 4 ')
new_list_5 = [el for el in my_list if el % 5 == 0]
print(f'{new_list_5} кратны 5 ')
new_list_6 = [el for el in my_list if el % 6 == 0]
print(f'{new_list_6} кратны 6 ')
new_list_7 = [el for el in my_list if el % 7 == 0]
print(f'{new_list_7} кратны 7 ')

