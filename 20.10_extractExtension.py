# Python Program to Extract Extension from the File Name
# In this Example, you will learn to extract extension from the file name

# Using the splittext() method from the os module
import os
extension = os.path.splitext('Saurabh.jpg')
print(extension)
print(extension[1])

# Using pathlib module: for the version 3.4, 3.5, 3.6(limit).
import pathlib
print(pathlib.Path('Saurabh.jpg'))
print(pathlib.Path('Saurabh.jpg').parent)
print(pathlib.Path('Saurabh.jpg').suffix)