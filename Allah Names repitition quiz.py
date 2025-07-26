
import random

# These are the two dictionaries we are quizzing from names and meanings respectively.
names = {
    1: "Ar-Rahman",
    2: "Ar-Raheem",
    3: "Al-Malik",
    4: "Al-Quddus",
    5: "As-Salam",
    6: "Al-Mu’min",
    7: "Al-Muhaimin",
    8: "Al-Aziz",
    9: "Al-Jabbar",
    10: "Al-Mutakabbir"
}

meanings1 = {
    1: "Nihayat Reham Karne Wala",
    2: "Behad Meharbaan",
    3: "Har Cheez Ka Malik",
    4: "Har Aib Se Pak",
    5: "Salamati Dene Wala",
    6: "Aman Dene Wala",
    7: "Nigraani Karne Wala",
    8: "Sab Par Ghalib",
    9: "Har Kami Ko Poora Karne Wala",
    10: "Buzurgi Dikhane Wala"
}


#This function generates a random number which will be the right choice and will be used later.
# def select_random_key():
#     k=random.randint(1,10)
#     return k
#
# right_key= select_random_key()
# print(right_key)
# print(type(right_key))

#this function generates wrong choices specifically 3 that will later be
# combined with the right choice.
def choice_generator():
    w_choice=set()
    c= random.sample(range(1,11),3)
    for i in c:
        w_choice.add(i)
    return w_choice

# choice=choice_generator()
# print(choice)
# print(type(choice))

# def preliminary_choices():
#     while True:
#         wrong_choices=choice_generator()
#         if right_key not in wrong_choices:
#             all_choices={right_key}.union(wrong_choices)
#             return all_choices,wrong_choices
#
# multiple_choice,w_choices=preliminary_choices()
# print(multiple_choice)


# def print_choices():
#     choice1 = meanings1.get(list(multiple_choice)[0])
#     choice2 = meanings1.get(list(multiple_choice)[1])
#     choice3 = meanings1.get(list(multiple_choice)[2])
#     choice4 = meanings1.get(list(multiple_choice)[3])
#     # print(f"1-{choice1}"
#     #       f"\n2-{choice2}"
#     #       f"\n3-{choice3}"
#     #       f"\n4-{choice4}"
#     #       )
#     return choice1,choice2,choice3,choice4
#
# choice_a,choice_b,choice_c,choice_d = print_choices()




def main():
    while True:


        def select_random_key():
            k = random.randint(1, 10)
            return k

        right_key = select_random_key()

        def preliminary_choices():
            while True:
                wrong_choices = choice_generator()
                if right_key not in wrong_choices:
                    all_choices = {right_key}.union(wrong_choices)
                    return all_choices, wrong_choices

        multiple_choice, w_choices = preliminary_choices()

        def print_choices():
            choice1 = meanings1.get(list(multiple_choice)[0])
            choice2 = meanings1.get(list(multiple_choice)[1])
            choice3 = meanings1.get(list(multiple_choice)[2])
            choice4 = meanings1.get(list(multiple_choice)[3])
            return choice1, choice2, choice3, choice4

        choice_a, choice_b, choice_c, choice_d = print_choices()



        print(f"What is the meaning of: {names[right_key]}\n")
        print(f"1-{choice_a}\n"
              f"2-{choice_b}\n"
              f"3-{choice_c}\n"
              f"4-{choice_d}\n")
        user_input=int(input("select one of the above options:\n"))
        while True:
            if user_input == 1:
                if choice_a == meanings1.get(right_key):
                    print("✅correct✅")
                    break
                else:
                    print("❌incorrect, try again❌")
                    break
            elif user_input == 2:
                if choice_b == meanings1.get(right_key):
                    print("✅correct✅")
                    break
                else:
                    print("❌incorrect, try again❌")
                    break
            elif user_input == 3:
                if choice_c == meanings1.get(right_key):
                    print("]✅correct✅")
                    break
                else:
                    print("❌incorrect, try again❌")
                    break
            elif user_input == 4:
                if choice_d == meanings1.get(right_key):
                    print("✅correct✅")
                    break
                else:
                    print("❌incorrect, try again❌")
                    break
        continue


main()