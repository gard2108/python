# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def sum():
    for i in range(4):
        end_list[i+1] += end_list[i] 
    res = end_list[4]
    return res

new_list = [randint(0,5) for i in range(10)]
print(new_list)

end_list = [item for i,item in enumerate(new_list) if i%2 != 0]
print(end_list)

print(sum())
