# 3. Реализуйте алгоритм перемешивания списка.

list = [1, 2, 3, 4, 5, 6, 7]
def list_change(list):
    list.sort(key = lambda x: x % 2)
    i = 1
    k = -1
    while i < len(list):
        list[i-1], list[k+1] = list[k+1], list[i-1]
        i += 1
        k -= 1
    return list
print(list_change(list))

