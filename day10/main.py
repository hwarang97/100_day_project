from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def show_operators(operations: dict):
    for key in operations:
        print(key)

def show_expression(operator: str, first_num: float, second_num: float, result):
    print(f"{first_num} {operator} {second_num} = {result}")


operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

print(logo)
first_number = float(input("What's the first number?: "))
is_continue = True
while is_continue:
    show_operators(operations)
    operator = input("Pick an operator: ")
    second_number = float(input("What's the second number?: "))
    result = operations[operator](first_number, second_number)
    show_expression(operator, first_number, second_number, result)
    keep_going = input("y|n: ")
    if keep_going == "n":
        is_continue = False
    else:
        first_number = result
