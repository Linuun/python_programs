# initialize an empty set to store numbers
numbers = []
# initialize a variable to store the sum
sum = 0
# ask user to input 10 numbers
print("Enter 10 numbers: ")
# use for loop
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
# add the number being input to the sum
    sum += num
# print sum