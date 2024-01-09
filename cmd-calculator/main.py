from art import logo

# calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
print(logo)
num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)

operational_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number?: "))

operation_func = operations[operational_symbol]
answer = operation_func(num1, num2)
print(f"{num1} {operational_symbol} {num2} = {answer}")


