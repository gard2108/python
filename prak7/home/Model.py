first = 0
second = 0
result = 0
choice = 0
example = 0
my_list = []
ind_first = 0
ind_second = 0

listOperator = {'*': lambda x,y: int(x) * int(y),
                '/': lambda x,y: int(x) / int(y),
                '+': lambda x,y: int(x) + int(y),
                '-': lambda x,y: int(x) - int(y)}

def init_choice(num_or_str: int):
    global choice
    choice = num_or_str

def set_first(number: int):
    global first
    first = number

def set_second(number: int):
    global second
    second = number

def set_result(oper: str):

    ### ДЕЛЕНИЕ НА НОЛЬ!!!!
    global result
    global second
    result = listOperator.get(oper)(first, second)


def get_first():
    global first
    return first

def get_second():
    global second
    return second

def get_result():
    global result
    return result

def get_choice():
    global choice
    return choice

def get_res_calc_examp(example: str):
    return result_example(res_in_skob(create_list(compact(example))))

def compact(example: str):
    if " " in example:
        example = example.replace(' ', '')
    return example

def create_list(example: str):
    global my_list
    example = (example.replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('/', ' / ')
                                                                .replace('(', '( ').replace(')', ' )'))
    my_list = example.split(' ')
    return my_list

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

def result_example(my_list: list):
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
