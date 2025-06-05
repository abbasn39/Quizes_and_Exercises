# Given a range of numbers using user inputs separate the odds and evens and print them separately.

Odd=[]
Even=[]
x=int(input("where do you want to start your range at?\n"))
y=int(input("where do you want to end your range at?\n"))


for i in range(x,y+1):
    if i%2==0:
        Even.append(i)
    else:
        Odd.append(i)

print("List of even numbers\n\t",Even)
print("List of Odd numbers\n\t",Odd)
