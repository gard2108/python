
# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

start = input('Введите форматируемую строку: ')

path = r'read.txt'
pathEnd = r'end.txt'

with open (path, 'w') as data:
        data.write(start)


with open (path, 'r')as data:
    text = data.readline()

if  ord(text[0]) > 57:        #если первый элемент строки - буква
    none = 'gg'
    text += none
    count = 1
    final = ''
    for i in range(len(text) -1):
        if (text[i] == text[i+1]):
            count += 1
        else:
            final += str(count) + text[i]
            count = 1
    with open (pathEnd, 'w') as data:
        data.write(final)
    print(final)
else: 
    count = 0
    num = ''
    final = ''
    for i in range(len(text)):
        if text[i].isdigit():
            num += text[i]
        else:
            final = final + text[i] * int(num)
            num = ''
    with open (pathEnd, 'w') as data:
        data.write(final)
    print(final)




            

        

