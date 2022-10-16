# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



start = 0
end = 0
flag = 1
count = 0

coll = 'Этот абвешный текст написан специально для удаления аабвешных слов.'
print(coll)

while (flag == 1):
    if ("абв" in coll):
        count += 1
        ind = coll.find('абв')
        for _ in range(len(coll)):
            if (ord(coll[ind]) != 32):     # ищу границы слова, находя "пробел" который в таблице юникода = 32
                ind -= 1
            else:
                start = ind
        ind = coll.find('абв')
        for _ in range(len(coll)):
            if (ord(coll[ind]) != 32):
                ind += 1
            else:
                end = ind
        coll = coll[:start] + coll[end:]
    elif(count > 1):
        flag = 0
        print(coll)
    else:
        flag = 0
        print('Такой подстроки в тексте нет.')        




