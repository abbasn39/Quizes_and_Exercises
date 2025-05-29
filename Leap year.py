# Make a program that checks if a year is leap. Use 'def' function.
#Hints:
# If year is not divisible by 4 it's not leap
# Years divisible by 100 are not leap unless they are divisible by 400 too.


def check_leap(year):
    if year%4==0:
        if year%100!=0:
            return f"the year {year} is a leap year"

        else:
            if year%400==0:
                return f"the year {year} is a leap year"

            else:
                return f"the year {year} is not a leap year"

    else:
        return f"the year {year} is not a leap year"



while True:
    user_input = input("Enter a year in XXXX format or type quit to exit: \n").strip() #.strip() avoids accidental spaces
    if user_input.lower() == "quit":
        print("Goodbye")
        break
    try:
        y=int(user_input)
        if y >=0:
            print(check_leap(y))
            continue
        elif y < 0:
            print("please enter a valid year")
            continue
    except ValueError:
        print("please enter a valid input")



