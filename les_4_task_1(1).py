# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
import timeit
import cProfile

X = 10
odd_number = 0
even_number = 0

while X > 0:
    if X % 2 == 0:
        even_number += 1
    else:
        odd_number += 1
    X = X // 10
print(f'Четные {even_number}, Нечетные {odd_number}')
#print(timeit.timeit('even_number', number=100, globals=globals())) # 10 цифр 8.211000000812874e-06
#print(timeit.timeit('odd_number', number=100, globals=globals()))  # 10 цифр 5.746999999445279e-06
#print(timeit.timeit('even_number', number=100, globals=globals())) # 20 цифр  9.031000001158418e-06
#print(timeit.timeit('odd_number', number=100, globals=globals()))  # 20 цифр  5.746999999445279e-06
#print(timeit.timeit('even_number', number=100, globals=globals())) # 30 цифр 9.441999999637574e-06
#print(timeit.timeit('odd_number', number=100, globals=globals()))  # 30 цифр 5.336999999272507e-06
#cProfile.run('even_number')
"""
(30)
3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
#cProfile.run('odd_number')
"""
3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

# рекурсия
def even_odd(number, even_=0, odd_=0):
    if number == 0:
        return even_, odd_
    if number % 2 == 0:
        even_ += 1
    else:
        odd_ += 1
    number = number // 10
    return even_odd(number, even_, odd_)

num = X
print(even_odd(num))

#print(timeit.timeit('even_odd(10)', number=100, globals=globals())) # 0.00014163299999836454
#print(timeit.timeit('even_odd(20)', number=100, globals=globals())) # 0.0001379379999999486
#print(timeit.timeit('even_odd(30)', number=100, globals=globals())) # 0.00013670600000104116

#cProfile.run('even_odd(300)')
"""
6 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      3/1    0.000    0.000    0.000    0.000 les_4_task_1(1).py:47(even_odd)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
1 решение - линейная сложность. Для данной задачи оптимально, ввод огромного количества цифр не подразумевается 
2 решение - квадратичная сложность
"""