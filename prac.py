arr = [13,7,6,12]
#TLE in higher cases because of two loops o(n**2)
for i in range(len(arr)-1):
    ele = arr[i]
    flag = False
    for j in range(i+1,len(arr)):
        if (arr[j]>ele):
            print(f"{ele} -> {arr[j]}")
            flag = True
            break
    if (flag==False):
        print(f"{ele} -> -1")

print(f"{arr[-1]} -> -1")