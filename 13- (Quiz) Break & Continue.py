#Quiz: Create a program that keeps asking for input until the user enters a number higher than 100.

# print("Your goal is to enter a number greater than 100")
# while True:
#     X = int(input("Your number please\n"))
#     if X>100:
#         print("Congratulations, this number is greater than 100")
#         break
#     if X==100:
#         print("This number is equal to 100 but try again")
#         continue
#     if X<100:
#         print("Please try again")
#         continue

#Question: Create a program that asks for a number between 1 and 10 only exits when the user enters
# a specific number(4)

# Guess=4
# print("I have thought of a number between 1 and 10 inclusive")
# print("Guess the number I'm thinking of")
# while True:
#     Number = int(input())
#     if 1<=Number<=10:
#         if Number==Guess:
#             print("Yes this is the number I thought of you must be a mind reader")
#             break
#         if Number!=Guess:
#             print("Guess again")
#             continue
#     else:
#         print("Please enter the number again in range 1-10")
#         continue

#Question: Loop through a list of number until you find a number that is divisible by 23.
List1=[1,2,3,34,5,6,66,55,33,23414,253,34,45,67]
i=0
while True:
    x = List1[i]
    if x % 23==0:
        print(x," is the first value divisible by 23")
        i=i+1
        break
    else:
        print(x)
    i=i+1


