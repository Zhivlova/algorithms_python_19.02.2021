"""
4. Определить, какое число в массиве встречается чаще всего.
"""
import random
import timeit
import cProfile

SIZE = 100
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
# меняем переменную SIZE, увеличиваем количество цифр в массиве
# print(timeit.timeit('my_func(array)', number=100, globals=globals()))    # (10)-    0.0006942059999999958
# print(timeit.timeit('my_func(array)', number=100, globals=globals()))   # (100) -  0.00677784699999999
# print(timeit.timeit('my_func(array)', number=100, globals=globals()))  # (1000) - 0.06447246700000002
# print(timeit.timeit('my_func(array)', number=100, globals=globals())) # (10000)- 0.40277321099999996
#cProfile.run('my_func(array)')
"""
(100)
104 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:14(my_func)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      100    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
{method 'get' of 'dict' objects} совпадает с количеством цифр в массиве 
"""


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

# меняем переменную SIZE, увеличиваем количество цифр в массиве
#print(timeit.timeit('most_common', number=100, globals=globals()))    # (10)- 1.1904999999992616e-05
# print(timeit.timeit('most_common', number=100, globals=globals()))   # (100) - 9.032000000006035e-06
# print(timeit.timeit('most_common', number=100, globals=globals()))  # (1000) - 8.20999999999461e-06
# print(timeit.timeit('most_common', number=100, globals=globals())) # (10000) - 8.210000000008488e-06
#cProfile.run('most_common')
"""
3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# третий вариант

import statistics
from statistics import mode

def most_common(array):
    return (mode(array))

print(most_common(array))

# меняем переменную SIZE, увеличиваем количество цифр в массиве
# print(timeit.timeit('most_common(array)', number=100, globals=globals()))    # (10)- 0.0010764090000000004
# print(timeit.timeit('most_common(array)', number=100, globals=globals()))   # (100) - 0.0026356010000000013
# print(timeit.timeit('most_common(array)', number=100, globals=globals()))  # (1000) - 0.009147834000000007
# print(timeit.timeit('most_common(array)', number=100, globals=globals())) # (10000)- 0.07503088200000002
# cProfile.run('most_common(array)')
"""
(100)
17 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 __init__.py:540(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:559(most_common)
        1    0.000    0.000    0.000    0.000 __init__.py:608(update)
        1    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
        1    0.000    0.000    0.000    0.000 heapq.py:521(nlargest)
        1    0.000    0.000    0.000    0.000 les_4_task_1.py:82(most_common)
        1    0.000    0.000    0.000    0.000 statistics.py:534(mode)
        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
"""
"""
Первый вариант.
Самый долгий и затратный. 
O(n) линейная сложность.  При увеличении размера списка 
выполняемая работа также пропорционально увеличивается.

Второй вариант.
O(1) константная сложность. Самый оптимальный: быстрый по времени и простой

Третий вариант.
Сложнее второго. 
O(1) константная сложность. При увеличении размера списка время 
выполнения программы незначительно увеличивается 
"""
