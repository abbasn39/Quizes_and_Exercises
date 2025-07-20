# Stock Available

candy=25
gum=25

while True:
    print("What can I get you?\n"
          "1- Select 1 for candy\n"
          "2- Select 2 for gum\n"
          "3- Press 3 to exit")

    d = int(input("Type selection\t\t"))
    if d==1:
        c=int(input("How many candies would you like?\t\t"))
        if candy ==0:
            print("Sorry we are out of stock")
        elif candy>0 and candy >= c:
            candy = candy-c
            print(c*"candy\t")
            print(f"candies remaining are {candy}")
        else:
            print("Please enter a valid number")
        continue
    elif d==2:
        g = int(input("How many gums would you like?\t\t"))
        if gum == 0:
            print("Sorry we are out of stock")
        elif gum > 0 and gum >= c:
            gum = gum - g
            print(g * "gum\t")
            print(f"candies remaining are {candy}")
        else:
            print("Please enter a valid number")
        continue

    elif d==3:
        print("Thank you for shopping here, please come again")
        break

    else:
        print("invalid selection please select again")
        continue