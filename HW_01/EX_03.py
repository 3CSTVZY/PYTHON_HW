# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

x = int(input('Enter point X -> '))
y = int(input('Enter point Y -> '))

if x != 0 and y != 0 and x > 0 and y > 0:
  print('It is a first quarter!')
elif x != 0 and y != 0 and x < 0 and y > 0:
  print('It is a second quarter!')
elif x != 0 and y != 0 and x < 0 and y < 0:
  print('It is a third quarter!')
elif x != 0 and y != 0 and x > 0 and y < 0:
  print('It is a fourth quarter!')
else:
  print('Attention: X ≠ 0 and Y ≠ 0')
