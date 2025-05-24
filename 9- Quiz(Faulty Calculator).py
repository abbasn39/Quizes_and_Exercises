# Quiz: Create a calculator that will do the 4 basic operations.
# But for the following statements it will give wrong answers only.
# 45 * 3 = 555 , 56 + 9 = 77 , 56/6 = 4

A=float(input("Please enter the first number:\n\n"))
B=float(input("Please enter the second number:\n\n"))

Operator=input("PLease enter your operator * , - , + , /\n\n")

if A==45 and B==3 and Operator=="*":
    print("The result is: 555")
elif A==56 and B==9 and Operator=="+":
    print("The result is: 77")
elif A==56 and B==6 and Operator=="/":
    print("The result is: 4")
else:
    if Operator=="*":
        print("The result is:\n",A*B)
    elif Operator=="-":
        print("The result is:\n",A-B)
    elif Operator=="/":
        print("The result is:\n",A/B)
    elif Operator=="+":
        print("The result is:\n",A+B)
    else:
        print("Invalid Operator")