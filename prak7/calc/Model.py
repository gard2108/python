import Control

a=0
b=0
c=''
temp = 0

def init_A(number:int):
    global a
    a=number

def init_B(number:int):
    global b
    b=number

def Get_A():
    global a
    return a

def Get_B():
    global b
    return b

def sum_data():
    global a
    global b
    return a+b

def vich_data():
    global a
    global b
    return a-b

def mult_data():
    global a
    global b
    return a*b

def div_data():
    global a
    global b
    return int(a/b)

def init_operation(charO:str):
    global c
    c=charO

def operator_choice():
    global a
    global b
    global c
    global temp
    if c == '+':
        temp = lambda a,b: int(a) + int(b)
        return temp
    if c == '-':
        return vich_data()
    if c == '*':
        return mult_data()
    if c == '/':
        return div_data()