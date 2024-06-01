# Python program to find the duplicate elements in a given string.
str = "sabvhgdhgfgdyt"
print(len(str))
list1 = []
list2 = []
for i in str:
    if i not in list1: 
        list1.append(i)
    else:
        list2.append(i)
# print(list1)
print("Duplicate Values are: ", list2)
print(len(list1))