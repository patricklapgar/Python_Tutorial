# What is a tuple
# A tuple is simply an ordered collection or grouping of items
# The difference here between a tuple and a list is that the items in a tuple
# are IMMUTABLE!!!!!
# Meaning, the values in a tuple CANNOT be changed

# This is a tuple
x = (1, 2, 3)
print(3 in x) # Returns True

# But wait! Why would you use a tuple
# Assuming you are only using values that won't change, tuples are way faster than lists
# They are more lightweight and they make you code safer from bugs
# You can also use tuples as keys within a dictionary
# Additionally, some methods return tuples to you such as the .items() method when working with dictionaries

# Example
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# When creating tuples there are two ways. First, use the () symbols
# or you can use the tuple function
# You can also use [] to access items within a tuple
print(months[-1]) # Returns December

# Again, tuples can also be used as keys in dictionaries but lists cannot

# ###############################################
# LOOPING AND TUPLE METHODS
# ###############################################
# You can use a for loop to iterate over a tuple just like a list!

names = ('Patrick', 'Alexandra', 'Toph', 'Katara', 'Aang', 'Sokka')
for name in names:
    print(name)

# You can also use a while loop
i = len(months) - 1
while(i >= 0):
    print(months[i])
    i = i - 1

# Several important methods to note are the count() method
# The count method returns the number of times a value appears in a tuple
names.count('Patrick') # Returns 1

# The next method is the index() method
# The index method returns the index at which a value is found in a tuple
names.index(1) # Returns 'Alexandra'

# You can also have nested tuples
nums = (1, 2, 3, (4, 5), 6)
nums[0] # Returns 1
print(nums[3][0]) # Returns 4

# And you can also use slices with tuples too
print(nums[0:4])