# Place Value of a number
number = int(input("Enter a number: "))
if (number>=1):
    rem_1 = number%10
    n_1 = rem_1/1
    print("Ones Place: ", n_1)
    number = number-rem_1
    
if (number>=10):
    rem_2 = number%100
    n_2 = rem_2/10
    print("Tens Place: ", n_2)
    number = number-rem_2

if (number>=100):
    rem_3 = number%1000
    n_3 = rem_3/100
    print("Hundred Place: ", n_3)
    number = number-rem_3

if (number>=1000):
    rem_4 = number%10000
    n_4 = rem_4/1000
    print("Thousand Place: ", n_4)
    number = number-rem_4

if (number>=10000):
    rem_5 = number%100000
    n_5 = rem_5/10000
    print("Ten Thousand Place: ", n_5)
    number = number-rem_5

if (number>=100000):
    rem_6 = number%1000000
    n_6 = rem_6/100000
    print("Lakh Place: ", n_6)
    number = number-rem_6

if (number>=1000000):
    rem_7 = number%10000000
    n_7 = rem_7/1000000
    print("Ten Lakh Place: ", n_7)
    number = number-rem_7

if (number>=10000000):
    rem_8 = number%100000000
    n_8 = rem_8/10000000
    print("Crore Place: ", n_8)
    number = number-rem_8


if (number>=100000000):
    rem_9 = number%1000000000
    n_9 = rem_9/100000000
    print("Crore Place: ", n_9)
    number = number-rem_9

if(number>=1000000000):
    print("Limit exceeded.")