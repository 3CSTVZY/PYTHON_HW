# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

a = int(input())
b = int(input())

# if a == b**2 or a**2 == b:
  # print(f'Digit is a square')
# else:
  # print(f'Digit is not a square')


if a == b**2:
  print(f'{a} square of {b}')
elif  b == a**2:
  print(f'{b} square of {a}')
else:
  print('NO')