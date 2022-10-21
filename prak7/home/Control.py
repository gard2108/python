from doctest import Example
import View,Model

def start():
    num_or_str = View.input_num_or_str()
    Model.init_choice(num_or_str)
    choice = Model.get_choice()
    if choice == 0:
        a = View.InputData('первое')
        Model.set_first(a)
        while True:
            oper = View.InputOperator()
            if oper == '=': break
            b = View.InputData('второе')
            Model.set_second(b)
            Model.set_result(oper)
            result = Model.get_result()
            if result == None:
                View.division_by_zero()
                break
            first = Model.get_first()
            second = Model.get_second()
            View.OutputResult(first, second, oper, result)
            # View.print_window(result)
            Model.set_first(result)
    else:
        example = View.input_string()
        result = Model.get_res_calc_examp(example)
        View.output_example_result(example, result)