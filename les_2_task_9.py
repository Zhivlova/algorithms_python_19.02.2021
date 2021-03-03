"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def sum_num(num):
    if num < 10:
        return num
    return num % 10 + sum_num(num // 10)

x = int(input("Вводите натуральные числа, для выхода нажмите 0 "))
max_sum = 0
max_num = 0
while x != 0:
    m = x
    a = sum_num(x)
    if a > max_sum:
        max_sum = a
        max_num = m
    n = int(input("Вводите натуральные числа: "))
print(f'Число {max_num} имеет сумму цифр, {max_sum}')