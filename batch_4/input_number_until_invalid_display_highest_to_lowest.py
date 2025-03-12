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
# check if the list contains number and display in it descending order
if numbers:
    numbers.sort(reverse=True)
    print(f"Here are the numbers from highest to lowest: {numbers}")
else:
    print("No numbers were entered")