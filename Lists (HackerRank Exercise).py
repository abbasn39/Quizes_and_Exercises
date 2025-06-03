# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


#The below solution is not for batch style input but user prompting inputs.(Haven't learned the other one yet hehe)
def smart_cast(value):
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except ValueError:
        return value

list1 = []

print("Please select one of the following options by typing:"
      "\n1) insert"
      "\n2) print"
      "\n3) remove"
      "\n4) append"
      "\n5) sort"
      "\n6) pop"
      "\n7) reverse"
      "\n8) exit"
      "\n")

while True:
    selection = input().strip().lower()

    if selection == "insert":
        x = smart_cast(input("Please enter the item you want to insert: \n"))
        y = int(input("Please enter the index number you want to insert at: \n"))
        list1.insert(y, x)
        print(list1, "current list")
        print("Select again or type 'exit' to quit")

    elif selection == "print":
        print(list1)
        print("Select again or type 'exit' to quit")

    elif selection == "remove":
        x = smart_cast(input("Please enter the item you want to remove: \n"))
        try:
            list1.remove(x)
            print(f"{x} removed from the list.")
        except ValueError:
            print(f"{x} not found in the list.")
        print(list1)
        print("Select again or type 'exit' to quit")

    elif selection == "append":
        x = smart_cast(input("Please enter the item you want to append: \n"))
        list1.append(x)
        print(list1)
        print("Select again or type 'exit' to quit")

    elif selection == "sort":
        try:
            list1.sort()
            print(list1)
        except TypeError:
            print("Cannot sort list with mixed data types.")
        print("Select again or type 'exit' to quit")

    elif selection == "pop":
        if list1:
            list1.pop()
            print("Last item removed from the list")
        else:
            print("List is already empty")
        print(list1)
        print("Select again or type 'exit' to quit")

    elif selection == "reverse":
        list1.reverse()
        print("List is now reversed")
        print(list1)
        print("Select again or type 'exit' to quit")

    elif selection == "exit":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid input, please try again.")