import numpy as np
# l = [1,2,3]
# l = np.array(l)
# print(l,type)

# l_2d = [[10,20,30],[40,50,60],[70,80,90]]
# l_2d = np.array(l_2d)
# print(l_2d)

# a = np.arange(0,100,3) #like range function
# print(a)

# zeors = np.zeros((4,4),dtype=int) #ones and zeros
# print(zeors,end = "\n\n") 

# b = np.linspace(0,100,50)
# print(b,end = "\n")

# c = np.random.randint(1,100,(10,10))
# print(c)

# identity = np.eye(4,5,dtype=int)
# print(identity,identity.dtype)


# alpha = "abcdefghijklmnopqrstuvwxyz"
# alpha = list(alpha)
# alpha = np.array(alpha)
# print(alpha)

# alpha.reshape(2,13)
# print(alpha)

# a = np.arange(0,100,2).reshape(2,25) * 5
# print(a,end = "\n\n")
# # print(a.sum(axis=0))

# print(a[0:,1:]/a[0:,1:])


# l = [2,6,7,9,5,3,5,2,7,6,5,1,3,2,2,8]
# counter = {}
# for i in l:
#     if i not in counter:
#         counter[i] = 1
#     else:
#         counter[i]+=1
# print(counter)

# l = []
# for i in range(1,10):
#     if i in counter:
#         for j in range(counter[i]):
#             l.append(i)
#     else:
#         continue
# print(l)


# import random as re
# import matplotlib.pyplot as plt
# import seaborn as sns
# l = []
# x = [i for i in range(10**6)]
# for i in range(1000):
#     for j in range(1000):
#         num = re.randint(0,1)
#         l.append(num)
# print(x,"\n\n\n",l)
# plt.bar(x,l)
# plt.show()
