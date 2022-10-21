import tkinter as tk

def input_num_or_str():
    num_or_str = int(input('Введите "1", если хотите ввести пример целиком или "0" если хотите вести счет поэтапно: '))
    return num_or_str

def InputData(string: str):
    number=int(input(f'Введите {string} число: '))
    return number

def OutputResult(a, b, oper, number):
    print(f'Результат операции {a} {oper} {b} = {number}')

def InputOperator():
    oper = input(f'Введите оператор: ')
    return oper

def division_by_zero():
    print('Деление на ноль!!')

# def print_window(result):
#     win = tk.Tk()
#     win.geometry('300x300+600+600')
#     my_label = tk.Label(win, text=result)
#     my_label.pack()
#     win.mainloop()

def input_string():
    example = input('Введите пример целиком: ')
    return example

def output_example_result(example, result):
    print(f'Результат выражения {example} = {result}')