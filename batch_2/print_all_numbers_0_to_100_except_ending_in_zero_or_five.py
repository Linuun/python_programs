# initialize an empty set to store numbers
numbers = []
# use for loop
for i in range(1, 101):
# process of eliminating numbers ending in zero or five
    if i % 5 != 0:
        numbers.append(i)
# print result