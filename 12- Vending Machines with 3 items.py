#This is a program for a vending machine that has 3 products: Candies, Chocolates and Crisps. It asks for the product
# customer wants and then the quantity of product needed. If the quantity demanded exceeds the available quantity then
# the program returns 'out of stock' after giving the quantity that was available.
# NOTE: This is not for multiple transactions as the available stock does not update, it's not a recurring program.

AvailableCandies=5
AvailableChocolates=5
AvailableCrisps=5
i=1

TypeofProduct=str(input("What can we get you today?"))
if TypeofProduct=="Candies":
    NumCandies=int(input("How many candies do you want?"))
    while i<=NumCandies:
        if i>AvailableCandies:
            print("Out of Stock")
            break
        print("Candy")
        i=i+1
    print("Thank you")
elif TypeofProduct=="Chocolates":
    NumChocolates = int(input("How many chocolates do you want?"))
    while i <= NumChocolates:
        if i>AvailableChocolates:
            print("Out of Stock")
            break
        print("Chocolates")
        i = i + 1

elif TypeofProduct=="Crisps":
    NumCrisps = int(input("How many crisps do you want?"))
    while i <= NumCrisps:
        if i>AvailableCrisps:
            print("Out of Stock")
            break
        print("Crisps")
        i = i + 1
    print("Thank you")
else:
    print("We do not have that in stock")