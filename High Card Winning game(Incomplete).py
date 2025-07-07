# import random
# J=10
# Q=11
# K=12
# A=13
# Cards= [2,3,4,5,6,7,8,9,10,J,Q,K,A]
#
#
# draw_card=random.choice(Cards)
# if draw_card == J or draw_card == Q or draw_card == K or draw_card == A:
#     print()
#
#
# print(draw_card)

import random
X={"A":10,"B":20}
print(X.items())
choice= random.choice(list(X.items()))
print(choice)
print(choice[0])
print(choice[1])