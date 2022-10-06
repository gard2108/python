
# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)


def negofibonacci(k):
    
    a, b = 1, 1
    for i in range(k):
        yield a
        a, b = b, a + b
k = 8
subSpis = []
count = 1

spis = list(negofibonacci(k))

for i in range(len(spis) * 2 + 1): 
    if (k%2 == 0 and count < k + 1):
        subSpis.append(pow(-1,count) * spis[k -i -1 ])
        count += 1
    elif (count == k + 1):
        subSpis.append(0)
        count += 1
    else:
        subSpis.append(spis[i - k - 1])
print(subSpis)
