import math
import abc
sum = 0
arr = [2,0,4,5,7]
print("Length of Array:", len(arr))
for sum in range (5):
    sum+=arr[sum]
    var1 = sum
    var2 = max(arr)
print("Sum of array:", var1)
print("Maximum value present in the Array =",var2)