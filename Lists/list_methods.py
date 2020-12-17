#########################################################################
# ADDITION METHODS ########################################################
#########################################################################

# Since working with lists is very common in Python development, there are a lot of different things you can do
# There are lots of different list methods that are useful

# The first is the append method
first_list = [1, 2, 3, 4]
first_list.append(5)
print(first_list) # [1, 2, 3, 4, 5]
# You can also append strings or numbers or booleans to the list

# The second method is extend
# The extend method adds of a list all values passed to the extend method
correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6, 7, 8])
print(correct_list) # [1, 2, 3, 4, 5, 6, 7, 8]

# The third method is insert
# You use this method to insert an item at a given position
first_list = [1, 2, 3, 4]
# The first parameter is the index at which you want to insert the value to
# The second parameter is the value that will be placed at that index
first_list.insert(2, 'Hi!')
first_list.insert(-1, 'The end!')
# So here's a special case. When you use the value -1, you are placing that value at the end of the old list. 

# For example:
# The line above will input the string 'The end!' at the last spot of the previous list which in this case is where the number 4 is
print(first_list) # [1, 2, 'Hi', 3, 'The end!' 4] and the list is extended

# To add a value at the very end of a list
nums = [1, 2, 3, 4]
nums.insert(len(nums), "LAST") # Here, you use the length method to add a string value at the lenght of the list, which is at the very end


#########################################################################
# REMOVE METHODS ########################################################
#########################################################################

# Another important list method is clear
# The clear method will remove all items from a list
random_list = [1, 2, 3, 4]
random_list.clear()
print(random_list) # []

# An alternative to clear is the pop method
# The pop method will remove the item at a given position on the list, and return it
# If no indedx is specified, the pop method will remove and return the last item in the list
random_list.pop() # returns 4
random_list.pop(1) # Returns 2

# Another method here is remove
# The remove method removes the first item from a list whose value is x
# Basically, you pass a parameter in the method, and it removes it
# If it can't find that value, however, then the method passes a ValueError

names = ["Patrick", "Alexandra", "Timothy", "Lesli", "Vanessa", "Patrick"]
names.remove("Patrick") # Returns ['Alexandra', 'Timothy', 'Lesli', 'Vanessa', 'Patrick']
print(names)

#########################################################################
# OTHER METHODS ########################################################
#########################################################################

# These ones are not as commonly used, but still important

# The first method is index
# The index method returns the index of a specified item in a list
nums = [5, 6, 7, 8, 9, 10]
print(nums.index(6)) # Returns 1
print(nums.index(9)) # 4

# You can also use multiple parameters here
nums.index(5, 1) # What this is saying is that the index method will look for the index of 5 starting after the 1st index of the array
nums.index(8, 6, 8) # Here, the index method will look for the index of 8 between the 6th and 8th indices
# The count method is very unique and could also be very helpful with algorithms and data structures
numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
# The count method iterates over a list and returns the number of times an element appears in a list
print(numbers.count(2)) # Returns 3 because the number 2 shows up 3 times in the array above

# Another useful method will be the reverse method
# This one is pretty obvious, it reverses the elements in a list
numbers.reverse()

# Here's a brief introduction to the sort method
# The sort method sorts the items of a list in ascending order
another_list = [6, 4, 1, 5, 3, 2]
another_list.sort()
print(another_list) # [1, 2, 3, 4, 5, 6]
# If you sort a list of strings, then it will order the strings in alphabetical order

# The last method here is the join method
# Although, the join method is not actually a list method, it is a string method
# However, it's commonly used to convert lists to strings
# The join method combines a copy of the base string between each item of the iterable
# And it also returns a new string

words = ['Coding', 'Is', 'Fun!']
# The first part right here before the join method is initiated is the base string
' '.join(words) # 'Coding Is Fun!'

