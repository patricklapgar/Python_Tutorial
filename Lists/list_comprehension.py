# List comprehensions are very powerful
# The idea is that list comprehensions are a very neat syntax that allow you to generate new lists
# The new lists are tweaked versions or direct copies of old lists

# ##############################################
# SYNTAX
# ##############################################

# Start with brackets
# [__ for __ in ___ ]
# Example
nums = [1, 2, 3]
[x*10 for x in nums] # Returns a new list with the values of [10, 20, 30]

# List Comprehension vs Looping
# Below is an example of looping
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for num in numbers:
    doubled_number = num * 2
    doubled_numbers.append(doubled_number)

print(doubled_numbers) # Returns [2, 4, 6, 8, 10]

# Vs that same code but with list comprehensions
# See! Less code, and it's much more clean
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)

# Another example involving strings
name = 'patrick'
[char.upper() for char in name]

friends = ['alexandra', 'vanessa', 'lesli']
result = [friend[0].upper() + friend[1:] for friend in friends] # Capitalizes the firs letter of every name
print(result)

# Yet another example but with ranges
[num * 10 for num in range(1, 6)] # Returns [10, 20, 30, 40, 50]

# And this one uses boolean values
[bool(val) for val in [0, [], '']] # Returns [False, False, False]

# This next one is useful and converts numbers to strings
numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)