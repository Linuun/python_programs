# ask user to input 2 numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# check if num2 is equal to zero
if num2 == 0:
    print("Error: Division by zero is not allowed")
# process of getting the quotient
else:
    quotient = num1 / num2
# print quotient
print(quotient)