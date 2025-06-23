print("This program will calculate the sum of natural numbers up to n(user defined)")
print("Iterative Approach\n")

def sum_naturals_iterative(x):
    a = 0
    for i in range(1,x+1):
        a= a + i
    return a

x=int(input("Enter a natural number: \n"))
print(sum_naturals_iterative(x))

# def sum_naturals_recursive(y):
#     if y==0:
#         return ("Enter a natural number please")
#     elif y==1:
#         return 1
#     else:
#         return y + sum_naturals_recursive(y-1)
#
#
# y=int(input("Enter a natural number: \n"))
# print(sum_naturals_recursive(y))