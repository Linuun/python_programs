# ask user to input 2 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# check if num1 is less than num2
if num1 < num2:
# use for loop
    for i in range(num1+1, num2):
# print result
        print(i)
# if num2 is less than num1 
else:
# use for loop
    for i in range(num2+1, num1)
# print result