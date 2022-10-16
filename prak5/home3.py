# 3. Создайте программу для игры в 'Крестики-нолики'.
                                                                                  


                                                                       # clicked СТАВИТ В ЯЧЕЙКУ КРЕСТИК ИЛИ НОЛИК И ВЫЗЫВАЕТ ПРОВЕРКУ НА ПОБЕДУ
                                                                                   #prov ПРОВЕРЯЕТ ВСЕ ВОЗМОЖНЫЕ КОМБИНАЦИИ ПОБЕДНЫЕ           
from tkinter import *
from random import randint as rI
from tkinter import messagebox

window = Tk()  
window.title("Охота за конфетами")   
window.geometry('260x300')

def clicked1():
    global count
    global pole
    if count == 0:
        btn1.configure( text='X')
        count += 1
        pole [0][0] = 'x'
        print (pole)
    else:
        btn1.configure( text='O')
        count -= 1
        pole [0][0] = 'o'
        print (pole)
    prov()
def clicked2():
    global count
    if count == 0:
        btn2.configure( text='X')
        count += 1
        pole [0][1] = 'x'
        print (pole)
    else:
        btn2.configure( text='O')
        count -= 1
        pole [0][1] = 'o'
        print (pole)
    prov()
def clicked3():
    global count
    if count == 0:
        btn3.configure( text='X')
        count += 1
        pole [0][2] = 'x'
        print (pole)
    else:
        btn3.configure( text='O')
        count -= 1
        pole [0][2] = 'o'
        print (pole)
    prov()
def clicked4():
    global count
    if count == 0:
        btn4.configure( text='X')
        count += 1
        pole [1][0] = 'x'
    else:
        btn4.configure( text='O')
        count -= 1
        pole [1][0] = 'o'
    prov()
def clicked5():
    global count
    if count == 0:
        btn5.configure( text='X')
        count += 1
        pole [1][1] = 'x'
    else:
        btn5.configure( text='O')
        count -= 1
        pole [1][1] = 'o'
    prov()
def clicked6():
    global count
    if count == 0:
        btn6.configure( text='X')
        count += 1
        pole [1][2] = 'x'
    else:
        btn6.configure( text='O')
        count -= 1
        pole [1][2] = 'o'
    prov()
def clicked7():
    global count
    if count == 0:
        btn7.configure( text='X')
        count += 1
        pole [2][0] = 'x'
    else:
        btn7.configure( text='O')
        count -= 1
        pole [2][0] = 'o'
    prov()
def clicked8():
    global count
    if count == 0:
        btn8.configure( text='X')
        count += 1
        pole [2][1] = 'x'
    else:
        btn8.configure( text='O')
        count -= 1
        pole [2][1] = 'o'  
    prov()
def clicked9():
    global count
    if count == 0:
        btn9.configure( text='X')
        count += 1
        pole [2][2] = 'x'
    else:
        btn9.configure( text='O')
        count -= 1
        pole [2][2] = 'o'
    prov()
                
def prov():
    for i in range (3):
        for j in range (3):
            if pole[i][0] == pole[i][1] == pole[i][2]:
                messagebox.showinfo('Поздравляем!', 'Игра окончена, вы победили!')
                break
            elif pole[0][j] == pole[1][j] == pole[2][j]:
                messagebox.showinfo('Поздравляем!', 'Игра окончена, вы победили!')
                break
            if pole[0][0] == pole[1][1] == pole[2][2]:
                messagebox.showinfo('Поздравляем!', 'Игра окончена, вы победили!')
                break
            elif pole[2][2] == pole[1][1] == pole[2][0]:
                messagebox.showinfo('Поздравляем!', 'Игра окончена, вы победили!')
                break
        
        
        
count = rI(0,1)
pole = [[0,1,2],
        [3,4,5],
        [6,7,8]]

btn1 = Button(window, text="",height = 6, width = 11, command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text="",height = 6, width = 11, command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text="",height = 6, width = 11, command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text="",height = 6, width = 11, command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text="",height = 6, width = 11, command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text="",height = 6, width = 11, command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text="",height = 6, width = 11, command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text="",height = 6, width = 11, command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text="",height = 6, width = 11, command=clicked9)
btn9.grid(column=3, row=3)



        




window.mainloop()

