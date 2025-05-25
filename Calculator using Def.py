#Make a program using 'def' function to create a calculator that takes 3 inputs from the user 2 numbers and a operator.
#Also for any function you define print a docstring for each for better readability of code.
def add_numbers(a,b):
    """This adds the two numbers"""
    result = a+b
    return result
def subtract_numbers(a,b):
    """This subtracts the two numbers"""
    result = a-b
    return result
def multiply_numbers(a,b):
    """This multiplies the two numbers"""
    result = a*b
    return result
def divide_numbers(a,b):
    """This divides the two numbers"""
    if b==0:
        return "infinite: Can't divide by zero"
    result = a/b
    return result

Number_1=int(input("Please enter the first number:\t"))
Number_2=int(input("Please enter the second number:\t"))
Operator_usage=input("Please enter the operator:\t(Add,Subtract,Multiply,Divide):\t)")

if Operator_usage=="Add":
    answer=add_numbers(Number_1,Number_2)
    print("Your answer is",answer)
elif Operator_usage=="Subtract":
    answer=subtract_numbers(Number_1,Number_2)
    print("Your answer is",answer)
elif Operator_usage=="Multiply":
    answer=multiply_numbers(Number_1,Number_2)
    print("Your answer is",answer)
elif Operator_usage=="Divide":
    answer=divide_numbers(Number_1,Number_2)
    print("Your answer is",answer)
else:
    print("Invalid input")
