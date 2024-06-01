# Armstrong Number are are those whose individual digit power(i.e.,power = equal to number of digits) sum is equal to that given number.
# Example - 1634 = 1^4 + 6^4 + 3^4 + 4^4
num = int(input("Enter a number = "))
leng = len(str(num))
sum = 0
assign = num
while(num!=0):
    rem = num%10
    sum = sum + (rem ** leng)
    num = num//10
print(sum)
print(assign)
if (sum == assign):
    print(f"{assign} is Armstrong Number.")
else:
    print(f"{assign} is not a Armstrong Number.")