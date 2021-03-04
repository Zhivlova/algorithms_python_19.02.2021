"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

def my_func(array):
    dict = {}
    count = 0
    itm = 0
    for item in array:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return (itm)

print(my_func(array))

# второй вариант
a_set = set(array)
most_common = None
num_most_common = 0

for i in a_set:
    num = array.count(i)
    if num > num_most_common:
        num_most_common = num
        most_common = i

print(most_common)

# третий вариант

import statistics
from statistics import mode

def most_common(array):
    return (mode(array))

print(most_common(array))
