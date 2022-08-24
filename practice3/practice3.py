# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
from typing import List

num_list = [1.1, 1.2, 3.1, 5, 10.01]
def sub (a):
    frac_list = list(filter(lambda x: x != 0, [round(i % int(i), 5) for i in a]))
    res = max(frac_list) - min(frac_list)
    return res
print(sub(num_list))

