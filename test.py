# if __name__ == '__main__':
#     key = []
#     val = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         key.append(name)
#         val.append(score)
#     # print(key,val)
    
#     s = list(set(val))
#     # print(s)
#     s.sort()
#     s = s[1]
#     # print(s)
#     for i in range(len(val)):
#         if (val[i]==s):
#             print(key[i])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # print("\n\n")
    # print(student_marks)
    print("%.2f" % float(sum(student_marks[query_name])/3))