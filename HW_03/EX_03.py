# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def minmax(list):
    maxi_mini = []
    for i in range(len(list)):
        if list[i]%1 != 0:
            maxi_mini.append(list[i]%1)
    return max(maxi_mini) - min(maxi_mini)

listPro = [1.10, 1.20, 3.10, 5, 10.01]
print(listPro)
result = minmax(listPro)
print(f'Difference between maximum and minimum fractional part = {result:.2f}')