# initialize an empty set to store numbers
numbers = []
# use for loop
for i in range(10):
# ask user to input 10 numbers
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)
# assigned the first number to a variable
result = numbers[0]
# process of subtracting the first number to the remaining
for num in numbers[1:]:
    result -= num
# print result
print(result)