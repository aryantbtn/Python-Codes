# Python Program to Merge Two Dictionaries.
# In this example, you will learn to merge two dictionaries into one in Python Programming.

# Using the | Operatior

dict_1 = {1:'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
print(dict_1 | dict_2)

# Using the ** operator -> This code will work with python 3.5 and 3.6 to know more about **kwargs
dict_3 = {3:'m', 4:'n'}
dict_4 = {5:'h', 9:'v'}
# print({dict_3, **dict_4})

# Using copy() and Update()
dict_5 = {2:'y', 4:'f'}
dict_6 = {6: 'u', 2:'e'}
dict_7 = dict_6.copy()
dict_7.update(dict_5)
print(dict_7)