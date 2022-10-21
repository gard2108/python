


stroka ='6-2/2*(8/2)/4+8'
my_list = []
ind_first = 0
ind_second = 0

def compact(stroka: str):
    if " " in stroka:
        stroka = stroka.replace(' ', '')
    return stroka

def div_on_0(): 
    if '/0' in stroka:
        print('Деление на ноль!!!')

def create_list(stroka: str):
    global my_list
    stroka = (stroka.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')
                                                                .replace('(', '( ').replace(')', ' )'))
    my_list = stroka.split(' ')
    return my_list

print(create_list(stroka))

listOperator = {'*': lambda x,y: int(x) * int(y),
                '/': lambda x,y: int(x) / int(y),
                '+': lambda x,y: int(x) + int(y),
                '-': lambda x,y: int(x) - int(y)}

def res_in_skob(my_list: list):
    global ind_first
    global ind_second
    if '(' in my_list: 
        for i,item in enumerate(my_list):
            if item == '(':
                ind_first = i
            if item == ')':
                ind_second = i
                for i in range(ind_first+2,ind_second-1,2):
                    my_list[i] = str(int(listOperator.get(my_list[i])(my_list[i-1],my_list[i+1])))
                    my_list.pop(ind_second)
                    my_list.pop(ind_second-1)
                    my_list.pop(ind_first+1)
                    my_list.pop(ind_first)
    return my_list


def result(my_list: list):
    while len(my_list) > 1:
        while '*' in my_list or '/' in my_list:
            for i,item in enumerate(my_list): 
                if item == '*' or item == '/':
                    my_list[i] = str(int(listOperator.get(my_list[i])(my_list[i-1],my_list[i+1])))
                    my_list.pop(i+1)
                    my_list.pop(i-1)
                    break
        while '+' in my_list or '-' in my_list:   
            for i,item in enumerate(my_list):
                if item == '+' or item == '-':
                    my_list[i] = str(listOperator.get(my_list[i])(my_list[i-1],my_list[i+1]))
                    my_list.pop(i+1)
                    my_list.pop(i-1)
                    break
        result = my_list[0]            
        return result



    



