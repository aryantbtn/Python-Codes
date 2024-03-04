# Python program to make a Simple Calculator
# In this example we will learn to create a simple calculator that can add, subtract, multiply or divide depending upon the input from the user.

# This functions add two numbers:
def add(x, y, d):
    return x+y+d

# This function subtract two numbers.
def subtract(a, b):
    return a-b

# This function multiply two numbers.
def multiply(u, v, w):
    return u*v*w

# This function divide two numbers.
def divide(m, n):
    return m/n

print("Select Operator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from user
    choice = input("Enter a choice(1/2/3/4): ")

    # Check if the choice is one of the four options or not:
    if choice in('1', '2', '3', '4'):
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the 3rd Number: "))
        if choice == '1':
            print(num1, "+" , num2, "+", num3, "=", add(num1, num2, num3))
        elif choice == '2':
            print(num1, "-" , num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*" , num2, "*", num3, "=", multiply(num1, num2, num3))
        elif choice == '4':
            print(num1, "/" , num2, "=", divide(num1, num2))
        
        # Check if the user want to do another calculation apart from the above operations.
        # Then we will break the while loop if the answer is no.
        next_calculation = input("Let's do a next Calculation? (Yes/No): ")
        if next_calculation == "No" or "no":
            break
    else:
        print("Invalid Input.")
