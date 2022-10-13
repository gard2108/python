# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10


temp = res = 56 #десятичное число
numN = 2
spis = []

while (temp > 0): 
    if (temp%2 != 0):
        temp = (temp - 1) / 2
        spis.append(1)
    else:
        temp = temp/2
        spis.append(0)

for i in range(len(spis)):
    if (int(len(spis))/2 < i + 1):
        break
    numN = spis[i]
    spis[i] = spis[-i-1]
    spis[-i-1] = numN
    
resN = str(spis[0] )

for i in range(1, len(spis)):
    resN += str(spis[i] )
print((f"число {res} в двоичной системме имеет вид {resN}"))


spis = []
spis.insert(0, 'num') - заполняет список с начала
join.spis - склеивает элементы с нужнм разделительным элементом