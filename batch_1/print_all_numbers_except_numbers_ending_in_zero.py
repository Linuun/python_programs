# initialize an empty set to store numbers
numbers = []
# use for loop
for i in range(1, 101):
# process of eliminating numbers ending in zero
    if i % 10 != 0:
        numbers.append(i)
# print result
print(numbers)