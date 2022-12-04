# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def pairs(list):
    listPro = []
    count = -1
    i = 0
    lenPro = len(list) / 2
    while i < lenPro:
        listPro.append(list[i]*list[count])
        count -= 1
        i += 1
    return listPro

list = [2, 3, 4, 5, 6]
list1 = pairs(list)
print(list)
print(list1)