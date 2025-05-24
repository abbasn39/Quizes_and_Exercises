#Exercise: Make a program that asks for input from the user. A predefined number is set
# The program tells the user to  go higher or lower until the correct guess is made.

Secret_Number=78
i=0

print("You have 10 guesses")
while True:
    i=i+1
    if i<=10:
        Guesses_left = 10 - i
        Number = int(input("Please enter your guess:\n"))
        if Number==Secret_Number:
            if i==1:
                print("congratulations your answer is correct and you still have all your guesses left")
            else:
                print(f"congratulations your answer is correct and you have {Guesses_left} guesses remaining")
            break
        if Number>Secret_Number:
            print(f"Go Lower please, you have {Guesses_left} guesses left")
            continue
        if Number<Secret_Number:
            print(f"Go Higher please, you have {Guesses_left} guesses left")
            continue
    else:
        print("you are out of guesses")
        break


#In line 14 where the program checks if "i=1", this means that when the user guesses the number on the first attempt
# the program will print the "... all guesses left" statement. 'i' is incremented on each attempt so when the user
# hasn't even guessed once it's value has already turned from 0 to 1 because of line 9.