# initialize an empty set to store numbers
numbers = []
# use while loop
while True:
# use try block
    try:
# ask user to input number
        num = int(input("Enter a number (or any non-numeric to stop): "))
        numbers.append(num)
# use except block to break the loop if the user inputs non-numeric
    except ValueError:
        break
# check the lowest number in the list and display
if numbers:
    print(f"The lowest number in the list is: {min(numbers)}")
else:
    print("No numbers were entered")