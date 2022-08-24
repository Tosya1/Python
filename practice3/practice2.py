#Напишите программу, которая найдёт произведение пар чисел списка. Парой 
# считаем первый и последний элемент, второй и предпоследний и т.д.

num_list = [2, 3, 5, 6, 7, 1, 2]

def mult_list (list):
    list1 = []
    i = 0
    k = -1
    while i < len(list) // 2 + len(list) % 2:
        list1.append(list[i]*list[k])
        i +=1
        k -= 1
    return list1
    
print(mult_list(num_list))


