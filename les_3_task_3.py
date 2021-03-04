"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

maximum = 0
minimum = 0
for i in range(len(array)):
    if array[i] < array[minimum]:
        minimum = i
    elif array[i] > array[maximum]:
        maximum = i
print(f'Индекс', minimum + 1, 'минимальное', array[minimum],'Индекс', maximum + 1, 'максимальное', array[maximum])
b = array[minimum]
array[minimum] = array[maximum]
array[maximum] = b

for i in range(len(array)):
    print(array[i], end=' ')
