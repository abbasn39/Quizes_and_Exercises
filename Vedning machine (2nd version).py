# Stock Available

candy=25
gum=25
# cost of stock
cost_candy=10
cost_gum=5
#cash input
cash=int(input("please insert cash:\t\t"))
while True:
    print("What can I get you?\n"
          "1- Select 1 for candy\n"
          "2- Select 2 for gum\n"
          "3- Press 3 to exit vending machine\n")

    if cash==0 or (cash<cost_candy not and cash<cost_gum):
        cash_selection=int(input(f"Your balance is low would you like to add more cash?\n"
              "1-Yes\n"
              "2-No\n"
              f"current cash: {cash}\n"
              f"selection:\t"))
        if cash_selection==1:
            cash = cash + int(input("Please insert cash:\t\t"))
        elif cash_selection==2:
            break
        else:
            print("Please enter a valid selection")
    else:
        d = int(input("Type selection\t\t"))
        if d == 1:
            c = int(input("How many candies would you like?\t\t"))
            if candy == 0:
                print("Sorry we are out of stock")
            elif cash<cost_candy:
                print("please add more cash")
                break
            elif candy > 0 and candy >= c:
                cash = cash - (c * cost_candy)
                candy = candy - c
                print(c * "candy\t")
                print(f"candies remaining are {candy}")
                print(f"remaining cash: {cash}")
            else:
                print("Please enter a valid number")
            continue
        elif d == 2:
            g = int(input("How many gums would you like?\t\t"))
            if gum == 0:
                print("Sorry we are out of stock")
            elif cash<cost_gum:
                print("please add more cash")
                break
            elif gum > 0 and gum >= g:
                cash = cash - (g * cost_gum)
                gum = gum - g
                print(g * "gum\t")
                print(f"gums remaining are {gum}")
                print(f"remaining cash: {cash}")
            else:
                print("Please enter a valid number")
            continue

        elif d == 3:
            print("Thank you for shopping here, please come again")
            break

        else:
            print("invalid selection please select again")
            continue