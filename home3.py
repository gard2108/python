# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []



from dis import findlabels
from random import randint as rI

dict = {}
finalStr = ''
stroka =''.join(list(map(str, [rI(0, 9) for i in range(20)])))
print(stroka)


for c in stroka:
    if dict.get(c):
        dict[c] = dict.get(c) + 1
    else:
        dict[c] = 1

for k,v in dict.items():
    if v == 1:
        finalStr += str(k) + ' '

print(finalStr)

