# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

# N = int(input('введите число - количество членов последовательности'))

# spisok = []
# for i in range(N):
#     spisok.append(pow(-3, i))
# print(spisok)

# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# from socket import create_server


# spis = []
# inStr = []
# spis = input('введите строку, проверяемую на вложенность: ')
# inStr = input('введите вкладываемую: ')

# count = 0
# result = 0

# for i in range (len(spis) - len(inStr) + 1): 
#     count = 0
#     for m in range (len(inStr)):
#         if (spis[i+m] == inStr[m]):
#             count += 1
#             if (count == len(inStr)):
#                 result += 1
# print(result)

# ИЛИ

# print(string.count(subString))

# ИЛИ 

# total = 0

# for i in range(len(string)-len(subString)+1):
# count = 0
# if string[i] == subString[0]:
# for j in range(len(subString)):
# if string[i+j] == subString[j]:
# count += 1
# if count == len(subString):
# total += 1

# print(f"Строка '{subString}' входит в строку '{string}' - {total} раз")

# ИЛИ

# counter = 0

# for i in range(len(string)):
# if string[i:i+len(subString)] == subString:
# counter += 1

# print(f'Количество вхождений - {counter}')


