import math
# Задача 3
# Найти расстояние между двумя точками пространства
# Вариант 1
x1 = int(input('Введите координату Х для первой точки: '))
y1 = int(input('Введите координату Y для первой точки: '))
z1 = int(input('Введите координату Z для первой точки: '))
x2 = int(input('Введите координату Х для второй точки: '))
y2 = int(input('Введите координату Y для второй точки: '))
z2 = int(input('Введите координату Z для второй точки: '))
dist = int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2))
print(f'Расстояние между двумя указанными точками {dist} ед.')

# Вариант 2
a = [
    int(input('Введите координату Х для точки A: ')),
    int(input('Введите координату Y для точки A: ')),
    int(input('Введите координату Z для точки A: '))
]
b = [
    int(input('Введите координату Х для точки B: ')),
    int(input('Введите координату Y для точки B: ')),
    int(input('Введите координату Z для точки B: '))
]
dist = int(math.dist(a, b))
print(f'Расстояние между двумя указанными точками {dist} ед.')
