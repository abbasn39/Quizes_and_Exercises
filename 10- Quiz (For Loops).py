print("Section 1")
#This program will check if the item is integer or float and is greater than, equal to or less than 6 and
# will print accordingly. If its a string it will print that its a string.
#This is only for item type int,float and str other datatypes are not included in this program.

# Random_List = [1, 3, 45, "John", 3.14, "What does the fox say?", 6, 77, 88, 1, 2,6.00]
# for item in Random_List:
#     if isinstance(item,int):
#         if item > 6:
#             print(item,"    is greater than 6 and is a type integer")
#         elif item==6:
#             print(item,"    is equal to 6 and is a type integer")
#         elif item < 6:
#             print(item,"    is less than 6 and it's an integer")
#     elif isinstance(item,float):
#         if item == 6.00:
#             print(item, "   is equal to 6 and is a type float")
#         elif item > 6:
#             print(item, "   is greater than 6 and is type float")
#         elif item < 6:
#             print(item,"    is less than 6 and it's a float")
#     else:
#         print(item,"    is a string")
#
print("Section 2")
#Quiz: Check every item in a list and if it's greater than or equal to 6 it will print otherwise it will not.
#The items may include more than one datatype.

List_Check=[1,5,4.1,66,8.88,2,3,4,55,6,"John","Matthew",3.14,5.5,9.9888]
for x in List_Check:
    if (isinstance(x,int) or isinstance(x,float) )and x>=6:
        print(x)
    pass

