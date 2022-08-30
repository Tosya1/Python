# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
# степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def get_k (max):
    k = randint(2, max)
    return k
# получить коэффициенты:
def get_ratios(k):
    ratios = [randint(0, 100) for i in range(0, k)]
    ratios.insert(0, randint(1, 100))
    return ratios

# получить многочлен
def get_polynomial (k, ratios):
    if ratios[0] !=1:
        pol = f'{ratios[0]}*x^{k}'
    else:
        pol = f'x^{k}'
    for i in ratios[1:]:
        if i != 0 and i != 1 and k > 2:
            pol += f' + {i}*x^{k-1}'
        elif i == 1 and k > 2:
            pol += f' + x^{k-1}'
        elif i != 0 and i != 1 and k == 2:
            pol += f' + {i}*x'
        elif i == 1 and k == 2:
            pol += f' + x'
        elif i != 0 and k == 1:
            pol += f' + {i} = 0'    
        elif i == 0 and k == 1:
            pol += f' = 0'  
        k -= 1
    return pol

# запись многочлена в файл
def write_pol (path, pol):
    with open(path, 'w') as data:
        data.write(pol)

k1 = get_k(10)
ratios1 = get_ratios(k1)
polynomial1 = get_polynomial(k1, ratios1)
write_pol('polynomial1.txt', polynomial1)
print(ratios1)
print(polynomial1)

k2 = get_k(10)
ratios2 = get_ratios(k2)
polynomial2 = get_polynomial(k2, ratios2)
write_pol('polynomial2.txt', polynomial2)
print(ratios2)
print(polynomial2)


