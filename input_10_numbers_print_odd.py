# initialize an empty set to store numbers
numbers = []
# initialize a variable to store odd numbers
odd = 0
# ask user to input 10 numbers
print("Enter 10 numbers: ")
# use for loop
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)
# process of knowing if a number is odd
    if num % 2 == 1:
# add 1 if the number is odd
        odd += 1
# print the total number of odd number/s