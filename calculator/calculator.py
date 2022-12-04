# calculator
def add(n1, n2):
    return n1+n2


def subtract(n1, n2):
    return n1-n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    # first input
    num1 = float(input("Type in your number 1: "))
    # second input
    for operator in operators:
        print(operator)

    should_continue = True
    while should_continue:
        symbol = input("Pick an operator: ")
        # third input
        num2 = float(input("Type in your second number: "))
        answer = operators[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        another_operation = input("Another operation? (Y) or new one (N)").upper()
        if another_operation == 'Y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
