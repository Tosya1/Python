# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

# проверка на простое число
def is_prime_num (n): 
    div_list = [ i for i  in range(2, n + 1) if n % i == 0 and n != i]
    if len(div_list) == 0:
        return True
    else: 
        return False

# получение простых множителей
def get_prime_fact (n):
    pf_list = []
    for i in range(2, n):
        if n % i == 0 and is_prime_num(i) == True:
            while n % i == 0:
                pf_list.append(i)
                n = n // i
    return pf_list

def show_ans (n):
    if is_prime_num(n) == True:
        print(f'{n} простое число, простой множитель {n}')
    else:
        print(f'Простые множители числа {n}: {get_prime_fact(n)}')

num = int(input('Задайте натуральное число N: '))
show_ans(num)