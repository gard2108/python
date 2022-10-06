# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

# res=0
# sum = 0

# num = float(input('введите дробное число с точкой: '))
 
# num =str(num)
# spis = num.split(".")
# res1 = int(spis[0])
# sum1 = 0
# sum = 0
# while ( res1 != 0):
#     sum1 = sum1 + res1 % 10
#     res1 = res1 // 10
# res = int(spis[1])
# while ( res != 0):
#     sum = sum + res % 10
#     res = res // 10
# print (sum + sum1)





# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

# count = 1
# res = 1
# N = int(input('введите число: '))
# print(res, end=", ")
# while (count != N - 1):
#     res = str(f"{res}*{count + 1}")
#     print(res, end=", ")
#     count += 1
# print(f"{res}*{count + 1}")





# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элеементов этой последовательности
#  (для проверки сумма для 4 элементов = 9,06 (примерно))

# spis = []
# sum = 0

# N = 1 + int(input('введите число: '))
# for N in range (1, N):
#     spis.append((1+1/N)**N)
# print(spis)
# for i in range(len(spis)):
#     sum += spis[i]
# print(sum)





# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него)
#  можно (нужно) использовать библиотеку Random

# import random

# spis = []

# res = 0

# N = int(input('введите число: '))

# for i in range(N):
#     spis.append(random.randint(-5,5))
# print(spis)

# res = random.sample(spis, N)
# print(res)


