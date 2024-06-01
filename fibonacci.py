a = 0
b = 1
n = int(input("Enter a number: "))
if n<0:
    print("Negative is not acceptable")
elif n==0:
    print(0)
elif n == 1:
    print(a)
else:
    for i in range(1, n+1):
        b = a+b
        print(a, end=" ")
        temp = b
        b = a
        a = temp