# initialize an empty set to store numbers
numbers = []
# use while loop
while True:
# use try block
    try: 
# ask user to input a number
        num = int(input("Enter a number (or any non-numeric to stop): "))
        numbers.append(num)
# use except block to break the loop if the user inputs non-numeric
    except ValueError:
        break
# check if the list contains number and display it in ascending order
if numbers:
    numbers.sort()
    print(f"Here are the numbers from lowest to highest: {numbers}")
else:
    print("No numbers were entered")