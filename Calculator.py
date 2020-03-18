#0.0.0.0
import Core_Functions as cf

def simple_addition(a, b):
    answer = a+b
    return answer


def simple_subtraction(a, b):
    answer = a-b
    return answer


def simple_multiplication(a, b):
    answer = a*b
    return answer


def simple_division(a, b):
    answer = a/b
    return answer


def simple_power(a, b):
    answer = a**b
    return answer


def run():
    cf.line("Current sum types: Addition, Subtraction, Multiplication, Division, Power")
    cf.line("Which sum type would you like to perform?")
    sum_type = cf.ask()
    if sum_type.lower() == "addition":
        a = cf.num_ask()
        b = cf.num_ask()
        c = simple_addition(a, b)
    elif sum_type.lower() == "subtraction":
        a = cf.num_ask()
        b = cf.num_ask()
        c = simple_subtraction(a, b)
    elif sum_type.lower() == "multiplication":
        a = cf.num_ask()
        b = cf.num_ask()
        c = simple_multiplication(a, b)
    elif sum_type.lower() == "division":
        a = cf.num_ask()
        b = cf.num_ask()
        c = simple_division(a, b)
    elif sum_type.lower() == "power":
        a = cf.num_ask()
        b = cf.num_ask()
        c = simple_power(a, b)
    cf.line(f"The answer is {c}")