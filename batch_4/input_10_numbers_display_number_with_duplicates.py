# define a function
def find_duplicates():
# initialize an empty set to store numbers
    numbers = []
# ask user to input 10 numbers
    print("Enter 10 numbers: ")
# use for loop
    for i in range(10):
        num = int(input(f"Enter a number {i+1}: "))
        numbers.append(num)
# check the numbers that appear more than once
    duplicates = sorted(set([num for num in numbers if numbers.count(num) > 1]))
# check if there are duplicates and display the numbers with duplicates