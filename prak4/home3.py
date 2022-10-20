# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []




from random import randint as rI

dict = {}
final_str = ''
stroka =''.join(list(map(str, [rI(0, 9) for i in range(20)])))
print(stroka)


for c in stroka:
    if dict(c) = 

for k,v in dict.items():
    if v == 1:
        final_str += str(k) + ' '

print(final_str)

