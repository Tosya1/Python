# Даны два файла в каждом из которых находится запись многочлена.
#  Сформировать файл содержащий сумму многочленов.
from dataclasses import replace
import re
from practice3 import get_polynomial, write_pol

# получить значение из файла
def read_pol (path):
    with open(path, 'r') as data: 
        for line in data:
            pol = line
        return pol
pol1 = read_pol('polynomial1.txt')
pol2 = read_pol('polynomial2.txt')    

# получить значения степень: коэффициет
def pol_to_dict(pol):
    pol = pol.replace(' = 0', '')
    pol = re.sub('[*|^|   ]', ' ', pol). split('+')
    pol =[i.strip().split(' ') for i in pol]
    pol_dict = {}
    for i in pol:
        if len(i) == 3:
            pol_dict[i[2]] = i[0]
        elif len(i) == 2 and i[0] == 'x':
            pol_dict[i[1]] = 1
        elif len(i) == 2 and i[0] != 'x':
            pol_dict['1'] = i[0]
        else:
            pol_dict['0'] = i[0]
    return pol_dict

pdict1 = pol_to_dict(pol1)
pdict2 = pol_to_dict(pol2)
print(pdict1)
print(pdict2)

# просуммировать коэффициенты 
def sum_ratios (dict1, dict2):
    sum_dict = {}
    for key in set(dict1).intersection(dict2):
        sum_dict[key] = int(dict1[key]) + int(dict2[key])
    for key in set(dict1).difference(dict2):
        sum_dict[key] = int(dict1[key])
    for key in set(dict2).difference(dict1):
        sum_dict[key] = int(dict2[key])
    sum_dict = sorted(sum_dict.items(), reverse = True)
    return sum_dict

pdict = sum_ratios(pdict1, pdict2)
print(pdict)
k1 = max([int(i[0]) for i in pdict])
print(k1)
ratios1 = [i[1] for i in pdict]
print(ratios1)
sum_pol = get_polynomial(k1, ratios1)
print(sum_pol)

write_pol('polynomial3.txt', sum_pol)