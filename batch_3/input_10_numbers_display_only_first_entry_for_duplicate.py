# define a function
def get_numbers_without_duplicates():
# initialize an empty set to store numbers
    numbers = []
# initialize a set to track numbers that are entered
    seen = set()
# ask user to input 10 numbers
    print("Enter 10 numbers: ")
# use for loop
    for i in range(10):
        num = int(input(f"Enter a number {i+1}: "))
# check if there are duplicates
        if num not in seen:
            seen.add(num)
            numbers.append(num)
# display all numbers excluding duplicates
    print(f"Here are the numbers (excluding duplicates): {numbers}")
get_numbers_without_duplicates()