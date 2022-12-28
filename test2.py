# import operator
# n = int(input())
# inp = []
# for i in range(n):
#     inp.append(input().split())

# # print(inp)

# ages = []
# for i in inp:
#     ages.append(int(i[2]))

# for i in range(len(ages)-1):
#     for j in range(i+1,len(ages)):
#         if (ages[i]>ages[j]):
#             ages[i],ages[j] = ages[j],ages[i]
#             inp[i],inp[j] = inp[j],inp[i]
# names = []

# for i in inp:
#     names.append(f"{i[0]} {i[1]}")
# print(names)

# s,n = input().split()
# count = 0

# for i in range(len(s)-len(n) + 1):
#     index = i
#     flag = False
#     for j in range(len(n)):
#         if (s[index]==n[j]):
#             # print(index,end = " ")
#             index+=1
#         else:
#             index = 0
#             break
#     if (index>0):
#         count+=1
# print(count)


# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # print(len(s))
# width = 4
# w = 0
# out = ''
# for i in range(len(s)):
#     if (w==width):
#         out+='\n'
#         out+=s[i]
#         w = 1
#     else:
#         out+=s[i]
#         w+=1
# print(out)

s = 5
# ind = 1
# for i in range(1,s+1):
#     for j in range(1,i+1):
#         print(j,end = "")
#     ind = j - 1
#     while (ind>=1):
#         print(ind,end = "")
#         ind-=1
#     print()

# Enter your code here. Read input from STDIN. Print output to STDOUT
# m = int(input())
# a = set(map(int, input().split()))
# n = int(input())
# b = set(map(int, input().split()))
# c = a.symmetric_difference(b)
# list(c).sort()
# for i in c:
#     print(i)

# n,m = list(map(int, input().split()))
# a = set(map(int,input().split()))
# b = set(map(int,input().split()))
# c = set(map(int,input().split()))  

# a = len(a.intersection(b)) - len(a.intersection(c))
# print(a)


# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import Counter
# x = int(input())
# sizes = list(map(int,input().split()))
# number_shoes_per_sizes = Counter(sizes).items()
# number_customers = int(input())
# xis = []
# for i in range(number_customers):
#     xis.append(list(map(int,input().split())))

# earned = 0
# keys_sizes = []
# val_shoes = []
# for i in number_shoes_per_sizes:
#     keys_sizes.append(i[0])
#     val_shoes.append(i[1])
# for i in xis:
#     for j in range(len(keys_sizes)):
#         if (i[0]==keys_sizes[j] and val_shoes[j]>0):
#             earned+=i[1]
#             val_shoes[j]-=1
#             break
# print(earned)


# n,m = list(map(int,input().split()))
# a = []
# b = []
# for i in range(n):
#     ele = input()
#     a.append(ele)
# # print(a)
# for i in range(m):
#     ele = input()
#     b.append(ele)


# for i in b:
#     flag = False
#     for j in range(len(a)):
#         if (a[j]==i):
#             flag = True
#             print(j+1,end = " ")
    
#     if (flag==False):
#         print(-1,end = "")
#     print()


# n = int(input())
# col_names = input().split()
# d = {}
# t_marks = []
# l = []
# for i in range(n):
#     row = input().split()
#     l.append(row)

# col_names = list(map(lambda x: x.lower(),col_names))
# # print(col_names)
# index = col_names.index('marks')
# for i in l:
#     t_marks.append(int(i[index]))
# # print(t_marks)
# t_marks = sum(t_marks) / len(t_marks)
# print(f"{t_marks:.2f}")


# n = int(input())
# names = []
# prices = []
# table = []
# for i in range(n):
#     row = input()
#     table.append(row)

# # print(table)
# for i in table:
#     num = ''
#     names_food = ''
#     for j in i:
#         if (j.isdigit()==True):
#             num+=j
#         elif (j.isalpha()==True):
#             names_food+=j
#         elif (j==" "):
#             names_food+=j
#     names.append(names_food)
#     prices.append(int(num))
# # print(names,prices)

# out = {}
# occur = []
# for i in range(len(names)):
#     if names[i] in out:
#         out[names[i]]+=prices[i]
#     else:
#         out[names[i]] = prices[i]
#         occur.append(names[i])

# for i in occur:
#     print(f"{i}{out[i]}")

# n = int(input())
# words = []
# for i in range(n):
#     word = input()
#     words.append(word)
# # print(words)

# d = {}
# for i in words:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i]+=1

# print(len(set(words)))
# for i in d.values():
#     print(i,end = " ")

# print("\n")


a = """
Hello 

I am 



Bhavye
"""

print(a)
# l = []
# for i in a:
#     l.append(i)

# print(l)
# print(list(a))