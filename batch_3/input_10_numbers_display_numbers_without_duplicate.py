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
# identify the numbers that appears only once
# display unique numbers