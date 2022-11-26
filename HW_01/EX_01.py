# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

a = int(input('Your day of the week (by digit): '))

if a in range(1, 6):
  print('This is not a rest day ;(')
elif a in range(6, 8):
  print('Your day off is here!')
else:
  print('Out of rang, hehe')