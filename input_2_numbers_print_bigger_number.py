# ask user to input 2 numbers 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# check if num1 is greater than num2
if num1 > num2:
    print (f"The bigger number is: {num1}")
# check if they are equal
elif num1 == num2 :
    print ("They are equal")
# check if num2 is greater than num1
else:
    print (f"The bigger number is: {num2}")


