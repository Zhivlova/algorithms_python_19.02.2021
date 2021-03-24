"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив {array}')

position = len(array) // 2
mediana = sorted(array)[position]
print('Медиана:',  {mediana})

