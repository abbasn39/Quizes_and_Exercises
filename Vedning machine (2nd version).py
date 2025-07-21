# Stock Available

candy=25
gum=25
# cost of stock
cost_candy=10
cost_gum=5
#cash input
balance = int(input("Please insert cash:\t\t"))
def cash(cash_in):
    global balance
    balance =balance + cash_in
    return print(f"Current Balance: {balance}")

while True:

    if balance==0 or balance < min(cost_candy,cost_gum):
        cash_selection=int(input(f"Your balance is low would you like to add more cash or exit?\n"
              "1-Add Cash\n"
              "2-Exit\n"
              f"current cash: {balance}\n"
              f"selection:\t"))
        if cash_selection==1:
            cash(int(input("Balance Low!! please insert cash:\t\t")))
        elif cash_selection==2:
            break
        else:
            print("Please enter a valid selection")
    else:
        print("What can I get you?\n"
              "1- Select 1 for candy\n"
              "2- Select 2 for gum\n"
              "3- Press 3 to exit vending machine\n")

        d = int(input("Type selection\t\t"))
        if d == 1:
            c = int(input("How many candies would you like?\t\t"))
            if candy == 0:
                print("Sorry we are out of stock")
            elif c > candy:
                selection=int(input(f"The current stock we have is {candy} candies"
                                    f"would you like to buy them all"
                                    f"1-Yes"
                                    f"2-No, I would like to choose again."
                                    f"3- Exit vending machine\n"))
                if selection == 1:
                    print("🍬"*candy)
                    candy = 0
                    continue
                elif selection == 2:
                    continue
                elif selection == 3:
                    break
                else:
                    print("Please enter a valid selection")
            elif balance< c*cost_candy:
                selection = int(input("Balance not enough for the purchase,please make a selection:\n"
                                      "1- Add more Cash\n"
                                      "2- Select different product\n"
                                      "3- Exit vending machine\n"))
                if selection == 1:
                    cash(int(input("Please insert cash:\t\t")))
                    continue
                elif selection == 2:
                    continue
                else:
                    break

            elif  candy >= c:
                balance = balance - (c * cost_candy)
                candy = candy - c
                print(c * "🍬\t")
                print(f"candies remaining are {candy}")
                print(f"remaining balance: {balance}")
            else:
                print("Please enter a valid number")
            continue
        elif d == 2:
            g = int(input("How many gums would you like?\t\t"))
            if gum == 0:
                print("Sorry we are out of stock")
            elif g > gum:
                selection=int(input(f"The current stock we have is {gum} candies"
                                    f"would you like to buy them all"
                                    f"1-Yes"
                                    f"2-No, I would like to choose again."
                                    f"3- Exit vending machine\n"))
                if selection == 1:
                    print("🫧"*gum)
                    gum = 0
                    continue
                elif selection == 2:
                    continue
                elif selection == 3:
                    break
                else:
                    print("Please enter a valid selection")
            elif balance< g*cost_gum:
                selection=int(input("Balance not enough for the purchase,please make a selection:\n"
                      "1- Add more Cash\n"
                      "2- Select different product\n"
                      "3- Exit vending machine\n"))
                if selection == 1:
                    cash(int(input("Please insert cash:\t\t")))
                    continue
                elif selection == 2:
                    continue
                else:
                    break

            elif gum >= g:
                balance = balance - (g * cost_gum)
                gum = gum - g
                print(g * "🫧\t")
                print(f"gums remaining are {gum}")
                print(f"remaining cash: {balance}")
            else:
                print("Please enter a valid number")
            continue

        elif d == 3:
            print("Thank you for shopping here, please come again")
            break

        else:
            print("invalid selection please select again")
            continue