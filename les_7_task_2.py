"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49

array = [round(random.uniform(MIN_ITEM, MAX_ITEM, ), 2) for i in range(SIZE)]
print(f'Исходный массив: {array}')

def merge_sort(array):
    def merge(left, right):
        result = []
        i = 0
        j = 0

        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:] if i < len(left) else right[j:])
        return result

    def div_half(lst):
        if len(lst) == 1:
            return lst
        elif len(lst) == 2:
            return lst if lst[0] <= lst[1] else lst[::-1]
        else:
            return merge(div_half(lst[:len(lst) // 2]), div_half(lst[len(lst) // 2:]))

    return div_half(array)


print('Отсортированный массив:', merge_sort(array))
