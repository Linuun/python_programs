# initialize a variable for the sum and count
total_sum = 0
count = 0
# use while loop
while True:
# use try block
    try:
# ask the user to input number
        num = int(input("Enter a number (or any non-numeric to stop): "))
# process of getting the sum of the numbers
        total_sum += num
# add 1 to the counter everytime a number is inputted
        count += 1
# use except block to break the loop if the user inputs non-numeric
    except ValueError:
        break
# process of getting the average and display it
if count > 0:
    average = total_sum / count
    print(f"The average of the numbers in the list is: {average}")
else:
    print("No numbers were entered")