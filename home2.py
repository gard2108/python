# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

spis =[]

i = 2 
N = int(input("введите число: "))

def naib_mn (n): 
    spis =[]

    i = 2
    while (n >= i): 
        if n % i : 
            i += 1 
        else: 
            n //= i 
            spis.append(i)
    return(spis)


print(naib_mn(N))
 

