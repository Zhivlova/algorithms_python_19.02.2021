"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, (len(array))):
    if array[i] < array[min1]:
        b = min1
        min1 = i
        if array[b] < array[min2]:
            min2 = b
    elif array[i] < array[min2]:
        min2 = i

print(f'Индекс', min1 + 1, 'минимальное число', array[min1])
print(f'Индекс', min2 + 1, 'минимальное число', array[min2])