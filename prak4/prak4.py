# import random

# size = random.randint(5,10)
# string = ''
# path = r'text.txt'
# pathWrite = r'newtext.txt'

# for _ in range(size):
#     string += f'{random.randint(1,9999)} '

# with open(path, 'w', encoding='UTF-8') as data:
#     data.write(string[:-1])

# with open(path, 'r', encoding='UTF-8') as data:
#     data_file = data.readline()


# file = data_file.split(' ')

# for i in range(len(file)):
#     file[i] = int(file[i])
# print(file)
# result = str(min(file)) + ' => ' + str(max(file))

# with open(pathWrite, 'w', encoding='UTF-8') as data:
#     data.write(data_file + '\n')
# data.write(result)


# ЗАДАЧА 2

path = r'text.txt'

A, B, C = input("Введите значение А, В, С через пробел: ").split()
A = int(A)
B = int(B)
C = int(C)


with open(path, 'w') as data:
    data.write(f"{A}*X**2 + {B}*X + {C} = 0")
with open(path, 'r') as data:
    file = data.readline()
print(file)

D = B**2 - 4*A*C
print(D)



задача 3 

mport math
import random
path = 'text.txt'
pathWrite = 'solve.txt'


with open(path, 'r', encoding='UTF-8') as data:
file = data.readline()


data_file = file.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('*x**2', '').replace('*x', '').split()


a = int(data_file[0])
b = int(data_file[1])
c = int(data_file[2])


discr = b**2 - 4*a*c

if discr>0:
x1 = (-b + math.sqrt(discr)) / (2 * a)
x2 = (-b - math.sqrt(discr)) / (2 * a)
result = f'X1 = {x1}, X2 = {x2}'
elif discr ==0:
x = -b / (2 * a)
result = f'X = {x}'
else:
result = 'Корней нет'

with open(path, 'a', encoding='UTF-8') as data:
data.write('\n' + result)


Список:  
for i in dict: - список ключей
for i in dict.values(): - список значений 
for i in dict.items(): вывод элементов в виде кoртежей
    print(i) или print(*i) - распаковывает кортеж

1) map(str(list)) - применяет фукнцию ко всем элементам списка (В СТРОКАХ)

2) ''.join(list) - склеивает элементы списка с заданным разделителем (В СТРОКАХ)

3) myList = list(map(lambda x: str(x) + '1', myList)) - добавляет в каждому элементу нужное( либо умножает и тд)

4) for i,k enumerate(list): - возвращает индекс нужного числа списка
    if K > 0
        print(i)
5) zip - создает список картежей из чисел с одинаковыми индексами в нескольких списках: 
list = myList(zip(list1, list2, list3))
