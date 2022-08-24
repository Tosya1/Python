# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов

from operator import index

number = int(input('Задайте число: '))

def fib (n):
    if n in [1, 2]:
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)

fib_list = [0]
for e in range(1, number + 1):
    fib_list.append(fib(e))
    if index(e) % 2 == 0:
        fib_list.insert(0, -fib(e))
    else:
        fib_list.insert(0, fib(e))
print(fib_list)

