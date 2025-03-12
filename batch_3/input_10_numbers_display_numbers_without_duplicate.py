# define a function
def get_unique_numbers():
# initialize an empty set to store numbers
    numbers = []
# ask user to input 10 numbers
    print("Enter 10 numbers: ")
# use for loop
    for i in range(10):
        num = int(input(f"Enter a number {i+1}: "))
        numbers.append(num)
# identify the numbers that appear only once
    unique_numbers = [num for num in numbers if numbers.count(num) == 1]
# display unique numbers
    print(f"Here are the unique numbers: {unique_numbers}")
get_unique_numbers()