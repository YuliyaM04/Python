#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А:')
xA = float(input('x: '))
yA = float(input('y: '))
print("Введите координаты точки B:")
xB = float(input('x: '))
yB = float(input('y: '))

from math import sqrt
print(round(sqrt((xA - xB)**2 + (yA - yB)**2), 2))