"""
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08)
[MSC v.1926 32 bit (Intel)] on win32
"""
import sys
from memory_profiler import profile

#@profile
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
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них 
кратны каждому из чисел в диапазоне от 2 до 9.
"""
result = {}
for n in range(2, 10):
    result[n] = []
    for f in range(2, 99):
        if f % n == 0:
            result[n].append(f)
    print(f'Для числа {n} кратны - {len(result[n])}. Кратные числа: {result[n]}.')

print('*' * 50)
"""
Для числа 2 кратны - 49 чисел. Кратные числа: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98].
Для числа 3 кратны - 32 чисел. Кратные числа: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96].
Для числа 4 кратны - 24 чисел. Кратные числа: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96].
Для числа 5 кратны - 19 чисел. Кратные числа: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95].
Для числа 6 кратны - 16 чисел. Кратные числа: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96].
Для числа 7 кратны - 14 чисел. Кратные числа: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98].
Для числа 8 кратны - 12 чисел. Кратные числа: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96].
Для числа 9 кратны - 10 чисел. Кратные числа: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90].
"""
print('*' * 50)
show(n)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
show(f)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=98
show(result)
"""
Словарь занимает 196 байт, и дополнительно 14 байт на каждый элемент.
Список занимает 260 байт, 168, 128, 128, 92, 92, 92, 92 
type(obj)=<class 'dict'>, sys.getsizeof(obj)=196, obj={2: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98], 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96], 4: [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96], 5: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95], 6: [6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96], 7: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98], 8: [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96], 9: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]}
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=2
type(obj)=<class 'list'>, sys.getsizeof(obj)=260, obj=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=2
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=6
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=8
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=14
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=16
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=18
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=20
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=22
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=26
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=28
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=32
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=34
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=38
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=44
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=46
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=48
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=50
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=52
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=58
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=60
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=62
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=64
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=66
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=68
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=70
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=74
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=76
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=78
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=80
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=82
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=86
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=88
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=92
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=94
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=96
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=98
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=3
type(obj)=<class 'list'>, sys.getsizeof(obj)=168, obj=[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=3
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=6
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=15
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=18
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=21
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=33
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=39
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=45
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=48
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=51
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=57
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=60
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=63
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=66
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=69
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=75
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=78
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=81
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=87
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=93
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=96
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=4
type(obj)=<class 'list'>, sys.getsizeof(obj)=128, obj=[4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=4
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=8
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=16
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=20
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=28
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=32
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=44
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=48
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=52
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=60
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=64
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=68
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=76
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=80
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=88
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=92
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=96
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=5
type(obj)=<class 'list'>, sys.getsizeof(obj)=128, obj=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=5
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=10
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=15
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=20
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=25
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=35
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=45
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=50
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=55
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=60
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=65
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=70
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=75
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=80
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=85
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=95
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=6
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=6
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=12
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=18
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=30
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=48
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=60
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=66
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=78
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=96
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=7
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=7
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=14
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=21
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=28
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=35
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=42
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=49
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=63
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=70
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=77
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=84
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=91
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=98
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=8
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=8
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=16
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=24
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=32
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=40
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=48
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=56
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=64
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=80
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=88
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=96
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=18
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=45
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=63
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=81
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
"""
show(result[n])
"""
Список занимает 92 байт, и дополнительно 14 байт на каждый элемент.
92+140
type(obj)=<class 'list'>, sys.getsizeof(obj)=92, obj=[9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=18
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=27
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=36
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=45
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=54
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=63
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=72
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=81
type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=90
"""
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     15.5 MiB     15.5 MiB           1   @profile
    10                                         def show(obj):
    11     15.5 MiB      0.0 MiB           1       print(f'{type(obj)=}, {sys.getsizeof(obj)=}, {obj=}')
    12     15.5 MiB      0.0 MiB           1       if hasattr(obj, '__iter__'):
    13                                                 if hasattr(obj, 'items'):
    14                                                     for key, value in obj.items():
    15                                                         show(key)
    16                                                         show(value)
    17                                                 elif not isinstance(obj, str):
    18                                                     for item in obj:
    19                                                         show(item)
"""
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     15.6 MiB     15.6 MiB           1   @profile
    30                                         def function():
    31     15.6 MiB      0.0 MiB           1       result = {}
    32     15.6 MiB      0.0 MiB           9       for n in range(2, 10):
    33     15.6 MiB      0.0 MiB           8           result[n] = []
    34     15.6 MiB      0.0 MiB          98       for f in range(2, 99):
    35     15.6 MiB      0.0 MiB          97           if f % n == 0:
    36     15.6 MiB      0.0 MiB          10               result[n].append(f)
    37     15.6 MiB      0.0 MiB           1       print(f'Для числа {n} кратны - {len(result[n])} чисел. Кратные числа: {result[n]}.')
"""
# вариант  без "массивов"
start_num = 2
end_num = 99
start_div = 2
end_div = 9

for i in range(start_div, end_div + 1):
    frequency = 0
    for j in range(start_num, end_num + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')

"""
Числу 2 кратно 49 чисел
Числу 3 кратно 33 чисел
Числу 4 кратно 24 чисел
Числу 5 кратно 19 чисел
Числу 6 кратно 16 чисел
Числу 7 кратно 14 чисел
Числу 8 кратно 12 чисел
Числу 9 кратно 11 чисел
"""
print('*' * 50)
show(start_num)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=2
print('*' * 50)
show(end_num)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=99
print('*' * 50)
show(start_div)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=2
print('*' * 50)
show(end_div)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=9
print('*' * 50)
show(frequency)
# type(obj)=<class 'int'>, sys.getsizeof(obj)=14, obj=11
"""
Ваш второй вариант самый экономичный и простой
"""