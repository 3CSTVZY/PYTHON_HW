# Напишите программу, которая на вход будет принимать число N и выводить числа от -N до N

a = int(input())

for i in range(-a, a+1):
  print(i, end=', ')