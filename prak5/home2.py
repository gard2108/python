
# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 1. Добавьте игру против бота
# 2. Подумайте как наделить бота 'интеллектом'
# Оба задания обязательны

from random import randint as rI
from tkinter import *
from tkinter import messagebox


window = Tk()  
window.title("Охота за конфетами")   
window.geometry('600x500')

totalKon = 150
player1 = 0
player2 = 0
count = 1


def clicked1():
    lb1.configure(text=f"Выпала цифра {rI(0,1)}")


def clicked2():  
    global totalKon
    global player1
    global player2
    global count
    if int(txt.get()) > 0 and int(txt.get()) < 29:
        totalKon -= int(txt.get())
        lb2.configure(text=f"Конфет осталось:{totalKon}")  
        if count % 2:
            player1 += int(txt.get())
            lb12.configure(text=f"Игрок 1: {player1}")  
            count += 1
            if totalKon == 0:
                lb13.configure(text=f"Игрок 2: 0")
                lb12.configure(text=f"Игрок 1: 150")  
                messagebox.showinfo('Поздравляем!', 'Победил игрок 1')
        else:
            player2 += int(txt.get())
            lb13.configure(text=f"Игрок 2: {player2}")  
            count += 1
            if totalKon == 0:
                lb12.configure(text=f"Игрок 1: 0")  
                lb13.configure(text=f"Игрок 2: 150") 
                messagebox.showinfo('Поздравляем!', 'Победил игрок 2')



lb0 = Label(window, text="Загадайте 0 или 1 и крутите барабан, кто угадал цифру, тот первый и ходит", font=("Arial Bold", 7))
lb0.grid(column=0, row=0) 
btn1 = Button(window, text="барабан", command=clicked1)
btn1.grid(column=1, row=0)
lb1 = Label(window, text=f"Выпала цифра ", font=("Arial Bold", 10))
lb1.grid(column=2, row=0) 

lb2 = Label(window, text=f"Конфет осталось:{totalKon}", font=("Arial Bold", 15))
lb2.grid(column=0, row=2) 
lb3 = Label(window, text=f"Сколько конфет вы хотите забрать: ", font=("Arial Bold", 15))
lb3.grid(column=0, row=3) 



txt = Entry(window,width=10, state='normal')  
txt.grid(column=1, row=3)
txt.focus()

btn = Button(window, text="забрать", command=clicked2)
btn.grid(column=1, row=4)

lb11 = Label(window, text="Количество конфет: ", font=("Arial Bold", 15))
lb11.grid(column=0, row=5) 
lb12 = Label(window, text=f"Игрок 1: {player1}", font=("Arial Bold", 15))
lb12.grid(column=0, row=6) 
lb13 = Label(window, text=f"Игрок 2: {player2}", font=("Arial Bold", 15))
lb13.grid(column=0, row=7) 



window.mainloop()

