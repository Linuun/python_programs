# initialize an emtpy set to store numbers
numbers = []
# initialize a variable to store even numbers
even = 0
# ask user to input 10 numbers
print("Enter 10 numbers: ")
# use for loop
for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)
# process of knowing if a number is even
    if num % 2 == 0:
# add 1 if the number is even
        even += 1
# print the total number of even number/s
print(f"The total even number/s is/are: {even}")