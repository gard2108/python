# Является ли число квадратом другого
#  a = int(input('one'))
# # b = int(input('two'))
# # if a == b * b or b == a * a:
# #     print('а - квадрат b')
# # else:
# #     print('a не квадрат b') 

# Какое из 5 введенных чисел максимальное

# spis = []
# for i in range(5):
#     spis.append(int((input('введите число'))))
# print(spis)

# max = spis[0]
# for i in range(len(spis)):
#     if max < spis[i]:
#         max = spis[i]
# print(max)

# Принимает число Н и выводит числа от -Н до Н

# N = int(input("введите число Н"))

# spis = []
# for i in range(N*2+1):
#     spis.append(int( i - N))
# print(spis)

# Принимает дробь и показывает первую цифру дробной части

# A = float(input("введите дробое число: "))
# print(int(A * 10 % 10))






# ДЗ 

# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да

# A = int(input('Введите число от 1 до 7,  где 1 - пнд, а 7 - вскр: '))
# if (A == 6 or A == 7 ):
#     print(f'{A} - да')
# else: 
#     print(f'{A} - нет')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# /
# /
# /
# /


# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=-34; y=-30 -> 3

# A = int(input('введите координату точки по оси X '))
# B = int(input('введите координату точки по оси Y '))

# if (A>0 and B>0):
#     print('1 четверть')
# elif (A>0 and B<0):
#     print('4 четверть')
# elif (A<0 and B>0):
#     print('2 четверть')
# elif (A<0 and B<0):
#     print('3 четверть')

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# A = int(input('введите номер четверти: '))

# if (A == 1):
#     print('X > 0, Y > 0 ')
# elif (A == 2):
#     print('X < 0, Y > 0 ')
# elif (A == 3):
#     print('X < 0, Y < 0 ')
# elif (A == 4):
#     print('X > 0, Y < 0 ')



# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7,21

# from math import sqrt


# sqrt((xb - xa) ^ 2 + (yb - yb) ^ 2)
# import math

# AX = int(input('введите координату точки А по оси X '))
# BX = int(input('введите координату точки А по оси Y '))
# AY = int(input('введите координату точки В по оси X '))
# BY = int(input('введите координату точки В по оси Y '))

# print (math.sqrt((BX - AX) ^ 2 + (BY - AY) ^ 2))

# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# A = int(input('введите число: '))

# if (A/5 == int(A/5) and A/10 == int(A/10) and A/30 != int(A/30)):
#     print('число кратно 5 и 10 но не кратно 30')
# elif (A/15 == int(A/15) and A/30 != int(A/30)):
#     print('число кратно 15 но не кратно 30')
# else:
#     print('число не подходит ни под одно условие')


