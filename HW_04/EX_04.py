# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

from random import randint
import random

k = int(input('Enter k: '))
result = ''
array = []
for i in range(k):
    array.append(randint(0, 100))

mark = ['+', '-']
i = 0
j = 0

while k > 1:
    if array[i] != 0:
        result += (f'{array[i]}x**{k}{random.choice(mark)}')
    k -= 1
    i += 1
if array[-1] != 0:
    result += (f'{array[-1]} = 0')
else:
    result += ('=0')
with open('result.txt', 'w', encoding='utf8') as file:
    file.write(f'Generated digits: {array}\nAnswer: {result}')