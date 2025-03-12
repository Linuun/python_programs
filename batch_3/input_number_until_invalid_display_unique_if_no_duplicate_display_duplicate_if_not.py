# define a function
def check_number_uniqueness():
# initialize an empty set to store numbers
    numbers = []
# use while loop
    while True:
# use try block
        try:  
# ask user to input a number 
            num = int(input("Enter a number (or any non-numeric to stop): "))
# check if the number is already in the list to determine if it is unique
            if num in numbers:
                print("Duplicate")
            else:
                print("Unique")
                numbers.append(num)
# use except block to break the loop if the user inputs non-numeric
        except ValueError:
            break
# display the result