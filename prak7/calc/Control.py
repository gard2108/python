import View,Model

def init_data():
    a = View.input_data('A')
    b = View.input_data('B')
    c = View.input_operation('C')
    Model.init_A(a)
    Model.init_B(b)
    Model.init_operation(c)

def print_values():
    a = Model.Get_A()
    b = Model.Get_B()
    View.output_data(a)
    View.output_data(b)

def print_operations():
    res = Model.operator_choice()
    View.output_result(res)

# def print_sum():
#     res = Model.sum_data()
#     View.output_result(res)

# def print_vich():
#     res = Model.vich_data()
#     View.output_result(res)

# def print_mult():
#     res = Model.mult_data()
#     View.output_result(res)

# def print_div():
#     res = Model.div_data()
#     View.output_result(res)

def init_operation():
    c = View.input_operation('C')
    res = Model.operator_choice(c)
    View.output_result(res)