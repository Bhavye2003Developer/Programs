# mutable -> list
# immutable -> tuple, dictionary, strings

import Employee

def list_oper():
    #List
    l1 = list({1,2,3,4})
    l1 = [1,3,4,5]
    print(l1)
    l1.append([1,4,5,6])
    print(l1)
    l1.remove(1)  #removes element error if not found
    print(l1)
    l1.pop() #removes last element error when list is empty
    print(l1)
    l1.insert(2,44)  # inserts element insert(index,element)
    print(l1)
    l1.sort(reverse=True) #sorts an array
    print(l1)
    l1.extend([23,55,67]) #extends list
    print(l1)
    l1.remove(l1[0])
    print(l1)
    # l2 = l1.copy()
    # print(l2)
    # l1.clear() #Empties the list
    # print(l1)
    print(l1.count(5))  #counts the element
    print(l1)
    print(f"Lenght : {l1}")
    print(f"index of 23 : {l1.index(23)}") #returns the index of element
    print(l1)
    # print(l1.count(12))
    l1.reverse() #does not return anything and only reverse the list like l.sort(reverse=True)
    print(l1)
    print(l1.__add__([10,20,30]))
def tuple_oper():

    #Tuples
    t1 = (12,34,5)
    # print(t1,type(t1))
    t1 = (12,34,5,)
    print(t1,type(t1))
    t1+=((13,)) #for concatenating tuple to tuple
    print(t1)
    t1 = t1 + (96,)
    print(t1)
    t1 = t1 + (23,45,6,7,86,85,86,86,12)
    print(t1)
    t1 = tuple(sorted(t1)) #returns sorted list in asc order
    print(t1)
    print(f"NUmber of times 86 occurs : {t1.count(86)}")
    print(t1.index(12)) #returns index of element in tuple error if not found
    print(t1.index(t1[-1]),len(t1))
def dict_oper():
    #Dictionary
    d1 = {"first":10,"second":[12,23,34,45,],"third":(12,23,45),"fourth":{12:21,23:32}}
    print(d1,end="\n\n")
    print(d1.get("second")) #get func returns value of key, if not found returns None
    d1.pop("second") #prints the key-val pair to be removed and removes it
    print("before : ",d1)
    # print("imp : " , list(d1.keys())[-1])
    d1.pop(list(d1.keys())[-1])
    # print(d1.pop("fourth"))
    # d1.keys()
    print("after : ",d1)
    print(d1.values()) #returns values of dictionary of type dict_values
    print(d1.get("first"), d1['first'])
    # print(d1.popitem()) #prints last element and removes it
    print(d1)
    d1['third'] = ([23],) + d1['third']
    print(d1)
    # d1.clear() #empties the dict
    d1.update({"fifth":{97,98,99,97,100}})
    print(d1,end = "\n\n")
    for i in d1.items():
        print(i)
    del d1["first"]
    print(d1)
    print("third" in d1)
def str_oper():
    s1 = "Hello world"
    print(s1)
    print(s1=="")
    print(s1.count("l")) #number of occurances
    print(s1.find("aa")) #returns the start index of substring if found else -1
    print(s1.capitalize())
    print(s1.upper())
    print(s1.lower())
    print(s1.title())
    print(s1.swapcase()) #returns string with all letters swapped lower to upper and upper to lower
    print(s1.replace("Hello","Good")) #returns a string with replaced keyword if found else return same string
    # s1 = "~".join(s1) #sepreates every element of iterabe object with character
    print(s1.isspace())
    # print(s1)
    print("\t".isspace()) #returns True if string only contains spacing characters
    print(s1.isdigit())
    print("123".isdigit()) #returns true if string contains only numbers
    a = s1.split(" ") #rturns a list having elements sperated with comma having sperators
    print(a)
    print(s1.startswith("h")) #returns true if string starts with character 'h'

e1 = Employee.Employee("Bhavye",99)
print(e1)
e1.show_info()