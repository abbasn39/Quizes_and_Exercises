#Square all numbers in a list.
a=[1,2,3,4,5]
square= lambda x: x**2

a_squared=[square(x) for x in a]
print(a_squared)

#Add 10 to numbers in a list
b=[1,2,3,4,5]
addition= lambda x:x+10

b_add_10=[addition(x) for x in b]
print(b_add_10)

#Filter Even numbers in a list
# c=[1,2,3,4,5,6,7,8,9,10]
# filter_even= lambda x:x%2==0
#
# c_filter_even=[filter_even(x) for x in c]
# for i in c_filter_even:
#     print[i]


