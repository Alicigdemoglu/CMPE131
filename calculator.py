def calculator(number1,number2,operator):
    if operator == "+":
        #add two numbers
        return(number1 + number2)
    elif operator == "-":
        #subtract two numbers
        return(number1 - number2)
    elif operator == "*":
        #multiply two numbers
        return(number1 * number2)
    elif operator == "/":
         #divide two numbers
        if number2 == 0:
            return False
        else:
            return(number1 / number2)
    elif operator == "//":
        if number2 == 0:
            return False
        else:
            return(number1 // number2)
    elif operator == "**":
        return(number1 ** number2)
    else:
        return False

# parse input fuction to validate operator and call calculation
def parse_input():
    n1=float(input("Enter the first number: "))
    n2=float(input("Enter the second number: "))
    op=input("Enter the operation: ")
    if not (op=="+" or op=="-" or op=="*" or op=="/" or op=="//"or op=="**"):
        return False
    calculator(n1,n2,op)
parse_input()