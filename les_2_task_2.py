"""
2. Посчитать четные и нечетные цифры введенного натурального числа. 
"""
x = int(input("Введите натуральное число: "))
odd_number = 0
even_number = 0

while x > 0:
    if x % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    x = x // 10
print(f'Четные {even_number}, Нечетные {odd_number}')