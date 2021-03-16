"""
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08)
[MSC v.1926 32 bit (Intel)] on win32
"""
import sys

def show(obj):
    print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)
print('*' * 50)

"""
В одномерном массиве целых чисел определить два наименьших элемента.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

if array[0] < array[1]:
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

print(f'Индекс', min1, 'минимальное число', array[min1])
print(f'Индекс', min2, 'минимальное число', array[min2])
"""
[6, 23, 64, 4, 13, 28, 99, 29, 97, 17]
Индекс 3 минимальное число 4
Индекс 0 минимальное число 6
"""
print('*' * 50)
show(SIZE)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=10
print('*' * 50)
show(MAX_ITEM)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=100
print('*' * 50)
show(MIN_ITEM)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=12, obj=0
print('*' * 50)
show(array)
"""
Список занимает 92 байт, и дополнительно 14 байт на каждый элемент.
92+140
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[6, 23, 64, 4, 13, 28, 99, 29, 97, 17]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=6
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=23
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=64
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=13
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=28
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=99
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=29
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=97
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=17
"""