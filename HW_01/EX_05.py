# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

ax = float(input('Please, enter coordinate of point A on the axis of X: '))
ay = float(input('Please, enter coordinate of point A on the axis of Y: '))
bx = float(input('Please, enter coordinate of point B on the axis of X: '))
by = float(input('Please, enter coordinate of point B on the axis of Y: '))

import math
distance = math.sqrt((ax-bx)**2+(ay-by)**2,)
print()
print(f'Distance between point A and B is = {distance}')
print()
print('\/ Answer below \/')
print(round(distance, 2))