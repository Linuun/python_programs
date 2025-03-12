# initialize an empty set to store numbers
numbers = []
# use while loop
while True:
# use try block
    try:
# ask user to input a number
        num = int(input("Enter a number(or any non-numeric to stop): "))
        numbers.append(num)
# use except block to break the loop if the user inputs non-numeric
    except ValueError:
        break
# look for the number with most duplicates and display
if numbers:
    frequency = {num: numbers.count(num) for num in set(numbers)}
    max_count = max(frequency.values())
    most_frequent = [num for num, count in frequency.items() if count == max_count]
    print(f"Number(s) with the most duplicates: {most_frequent}")
else:
    print("No numbers were entered")
