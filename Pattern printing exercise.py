# Print a pattern using an input
# n is an integer input from the user which defines the numbers of rows
# The rows will have asterisk printed in then in ascending or descending order depending on another  input from the user
# Ask user for a 1 or 0 input representing True and False Boolean input
# if True program will print asterisk by rows starting form 1 * and ending with n * with each row having 1 more than the
# previous row(Ascending order) and opposite for False ie Descending order
# n = 4 Bool= True
#Print:
# *
# **
# ***
# ****

# n=5 Bool= False
# Print:
# *****
# ****
# ***
# **
# *

#Solution

try:
    Order = int(input("Please enter 1 for Ascending and 0 for Descending order: \n"))

    n = int(input("Please enter the number of rows you want in the pattern:\n"))
    i = 0
    if Order!=0 and Order!=1:
        print("Please enter correct value for Order ie 1 or 0")

    elif n<=0:
        print("Please enter a non-negative integer")

    if Order==1 and n>0:
        while True:
          if i==n+1:
              break
          else:
              print("*"*i)
              i=i+1
              continue

    elif Order==0 and n>0:
        while True:
          if n==i:
              break
          else:
              print("*"*n)
              n=n-1
              continue
except ValueError:
    print("invalid input")


# I haven't used bool typecasting because it seemed redundant but I will look into this option as well.