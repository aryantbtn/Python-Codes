# Python program to add 2 Matrices.
# In this program, you'll laern to add two matrices using Nested loop and Next list comprehension, and display it.

# Matrix add through Nested loop
'''x = [[1520, 8845, 62, 51], [84, 56, 3, 12], [56, 202, 562, 620], [541, 563, 959, 562]]
y = [[74, 625, 489, 764], [72, 871, 32, 625], [72, 565, 68, 19], [290, 66, 553, 827]]
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# iterate through rows:
for i in range(len(x)):
    # iterate through columns
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
    print(r)'''

# now by using the matrix addition now by using the nested list comprehension:
'''x = [[1520, 8845, 62, 51], [84, 56, 3, 12], [56, 202, 562, 620], [541, 563, 959, 562]]
y = [[74, 625, 489, 764], [72, 871, 32, 625], [72, 565, 68, 19], [290, 66, 553, 827]]
result = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
for r in result:
    print(r)'''