import numbers


def input_data(number):
    number = int(input(f'Введите число {number}: '))
    return number

def output_data(number):
    print(f'Число {number}')

def output_result(number):
    print(f'Результат операции = {number}')

def input_operation(charO):
    charO = str(input(f'Введите оператор {charO}: '))
    return charO