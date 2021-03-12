import timeit
import cProfile

n = int(input("Вывод простых чисел до числа ...  "))
lst = [2]
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j * j - 1 > i:
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print(f'все простые числа от 2 до {n} {lst}')

#print(timeit.timeit('lst', number=100, globals=globals())) # (10) 1.3137000000273957e-05
#print(timeit.timeit('lst', number=100, globals=globals())) # (100) 7.800000000113272e-06
#print(timeit.timeit('lst', number=100, globals=globals())) #(1000) 5.336999999716596e-06
#print(timeit.timeit('lst', number=100, globals=globals())) #(10000) 5.3370000001606854e-06
#cProfile.run('lst')
"""
3 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

n = int(input("Вывод простых чисел до числа ...   "))
sieve = set(range(2, n + 1))
while sieve:
    prime = min(sieve)
    print(prime, end="\t")
    sieve -= set(range(prime, n + 1, prime))

#print(timeit.timeit('prime', number=100, globals=globals())) # (10) 8.209999999841955e-06
#print(timeit.timeit('prime', number=100, globals=globals())) # (100) 1.3135999999747128e-05
#print(timeit.timeit('prime', number=100, globals=globals())) # (1000) 7.799999999669183e-06
#print(timeit.timeit('prime', number=100, globals=globals())) # (10000) 7.799999998781004e-06
#cProfile.run('prime')
"""
Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""