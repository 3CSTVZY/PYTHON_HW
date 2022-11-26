# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

a = int(input('Enter the number of quarter: '))
if a == 1:
  print('Your answer is: x > o, y > o')
elif a == 2:
  print('Your answer is: x < o, y > o')
elif a == 3:
  print('Your answer is: x < o, y < o')
elif a == 4:
  print('Your answer is: x > o, y < o')
else:
  print('Out of range, bro')