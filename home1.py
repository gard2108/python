# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001




from decimal import Decimal
import math

count = 0

d = input("введите числе, отражающее количество знаков после запятой вида '0.0...01: ")
spis = d.split('.')
num = spis[1]

for i in range(len(num)):
    count += 1

res = Decimal(f'{round(math.pi, count)}')
print(res)






