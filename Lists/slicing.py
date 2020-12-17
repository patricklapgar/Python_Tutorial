# Slicing is a built-in tool that allows you to make either entire copies of a list
# or a copy of a portion of a list (this method can also slice strings, but the focus will be placed on lists for now)

# Slice isn't a method that you can call with a dot 
# You can make lists using the slices of the old list
# some_list[start:end:step]
nums = [1, 2, 3, 4, 5, 6, 7]
nums[1:] #[2, 3, 4, 5, 6, 7]
# print(nums[3:]) # [4, 5, 6, 7]

# You can also slice from the end using -1
print(nums[-1:]) # [7]

# Using the second parameter
nums[1:4] # [2, 3, 4]
nums[:2] # [1, 2]
nums[:4] # [1, 2, 3, 4]


# Lastly is the third parameter for step
nums[1::2] # [2, 4, 6]
nums[::2] # [1, 3, 5, 7]

nums[1::-1] # [2, 1]
nums[:1:-1] # [6, 5, 4, 3]
nums[2::-1] # [3, 2, 1]

# Ex:
string = "Coding is fun"
print(string[::-1]) # Returns nuf si gnidoC

numbers = [1, 2, 3, 4, 6]
numbers[2:3] = ['a', 'b', 'c']

print(numbers)

# Interestingly, you can also swap values using special syntax with commas
# This is very useful when you're shuffling lists and so forth
# It is also useful with sorting, and also algorithms
names = ["Patrick", "Alexandra"]
names[0], names[1] = names[1], names[0]
print(names) # ['Alexandra', 'Patrick']

# An example
def capitalize(string):
    """ A function that returns the inputted string but with the first letter capitalized """
    return string[0].upper() + string[1:]