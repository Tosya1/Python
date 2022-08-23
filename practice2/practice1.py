# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from functools import reduce

a = input('Введите число: ').replace('.', '')
sum = reduce(lambda x, y: x + y, [int (x) for x in a])
print(sum)