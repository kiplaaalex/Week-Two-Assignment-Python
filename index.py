# Create an empty list
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


my_list.insert(1, 15)


my_list.extend([50, 60, 70])


my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")

# Optionally, print the final list
print("Final sorted list:", my_list)
