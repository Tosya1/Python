# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

from functools import reduce

num_list = [1, 2, 3, 4, 5, 6, 7]
odd_sum = reduce(lambda x, y: x + y, num_list[1::2])
print(odd_sum)