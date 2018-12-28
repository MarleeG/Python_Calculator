# Intro
def intro():
    print('I am the calculator app!')

# Operations
def add(n1, n2):
    print(n1+n2)
    anotherCalculation()

def subtract(n1, n2):
    if n1 < n2:
        print(n2-n1)
    else: 
        print(n1-n2)
    anotherCalculation()

def multiply(n1, n2):
    print(n1*n2)
    anotherCalculation()

def divide(n1, n2):
    if n1 < n2:
        print(n2/n1)
    else: 
        print(n1/n2)
    anotherCalculation()

# This will give you the option to complete another application
def anotherCalculation():
    print('--------------------------------------------')
    print('Type Y or N')

    again = raw_input('Would you like to complete another calculation?')

    if again == 'Y' or again == 'y':
        operationSelection()
    else: print('Goodbye!')
        
    
# Select the two numbers you would like to use for the calculation
def chooseNums(operator):
    num1 = input('Enter your first number: ')
    num2 = input('Enter your second number: ')

    if operator == '+':
        add(num1, num2)
    elif operator == '-':
        subtract(num1, num2)
    elif operator == '*':
        multiply(num1, num2)
    else: divide(num1, num2)


# Select an operator using this function
def operationSelection(valid_op = True):
    print('--------------------------------------------')
    if valid_op == False:
        print('Please type one of the valid operators listed below')

    print('Operators: + - * /')
    print('Choose an operation you would like complete.')
    # print('Type one of these: add subtract multiply divide')
    operator = raw_input()

    if operator == '+' or operator == '-' or operator == '*' or operator == '/':
        chooseNums(operator)
    else: 
        operationSelection(False)


def main():
    intro()
    operationSelection()

main()