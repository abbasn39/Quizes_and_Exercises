#----------Stock----------
candy=25
gum=25
cost_candy=10
cost_gum=5
# ----------Integer Error Handling ----------
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter integer only.")


# ----------View stock----------
def view_stock(item):
    while True:
        stock_selected = get_int_input("Select one of the following number: \n"
                                       "1- Candy\n"
                                       "2- Gum\n"
                                       "3-Exit\n")
        if stock_selected == 1:
            print("Stock left:\t\t", candy)
        elif stock_selected == 2:
            print("Stock left:\t\t", gum)
        elif stock_selected == 3:
            break
        else:
            print("Please enter integer only.")
            continue

#----------purchase----------
def purchase_stock(item):

    item_selected = get_int_input(f"Select one of the following number: \n"
                                  f"1- Candy for {cost_candy}\n"
                                  f"2- Gum for {cost_gum}\n"
                                  "3-Exit\n")
    if item_selected == 1:
        quantity = get_int_input(f"How many candies would you like to purchase?\n")

