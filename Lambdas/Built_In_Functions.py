# The first function to learn is map()
# map() is a standard function that accepts two arguments
# - a function as one parameter
# - an iterable as the second parameter (i.e strings, lists, dictionaries, sets, and tuples)

# The map() function runs the lambda for each value in the iterable and returns a map object

# Example
nums = [2, 4, 6, 8, 10]
doubles = map(lambda num: num * 2, nums)
print(list(doubles))

# Another example
people = ["Darcy", "Patrick", "Alexandra"]
peeps = map(lambda name: name.upper(), people)
print(list(peeps))

# Yet another example but this time w/ a list of of dictionaries
names = [
    {'first': 'Patrick', 'last': 'Apgar'},
    {'first': 'Alexandra', 'last': 'Chheng'},
    {'first': 'Timothy', 'last': 'Apgar'}
]

first_names = list(map(lambda name: name['first'], names))
print(first_names)

# One more example
def decrement_list(numbers):
    new_nums = map(lambda num: num - 1, numbers)
    return list(new_nums)

print(decrement_list([1, 2, 3]))

# The next function is filter()
# In the filter() function, there is a lambda for each value passed into the function. 
# Typically, filter() returns an object, but it can be converted to other iterables like lists and so forth
# Note: The object contains only the values that return true to the lambda

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Example
# Write a function that takes both a list and a letter as parameters
# return a list with the first letter matching the input 

arr_of_names = ["Patrick", "Patrice", "pierre", "Alexandra", "Albert", "Christopher"]

def return_names(names, first_letter):
    result = list(filter(lambda name: name[0].lower() == first_letter.lower(), names))
    return result

print(return_names(arr_of_names, 'P'))

# Another Example
users = [
    {"username": "samuel", "tweets": ["Hello, Happy Birthday, Good Morning"]},
    {"username": "patrick", "tweets": ["Hello, Happy Birthday, Good Morning"]},
    {"username": "alexandra", "tweets": []},
    {"username": "jeff1234", "tweets": []},
    {"username": "sammy_cat", "tweets": ["Hello, Happy Birthday, Good Morning"]},
    {"username": "Mr.Dog", "tweets": []}
]

inactive_users = list(filter(lambda user: not user['tweets'], users))
# You could do the same thing and more using both map() and list()
usernames = list(map(
    lambda user: user["username"], 
    filter(lambda user: not user['tweets'], users)
))
# Here's the same thing as a list comprehension
print([user for user in users if not user["tweets"]])
print([user["username"] for user in users if not user["tweets"]])
print(inactive_users)

# #############################################
# Combining filter() and map()
# #############################################
# Example

# Given this list of names:
names = ["Patrick", "Alexandra", "Rusty"]
# Return a new list with the string "Your instructor is " + each value in the array 
# but only if the value is less than 5 characters

# Note, you can use filter() within map()
result = list(map(
    lambda name: f"Your instructor is {name}", 
    filter(lambda value: len(value) < 5, names)
))

print(result)

# Another Example

# accepts a list of numbers
# filter for each number if it is greater than -1
# return filtered list

def remove_negatives(nums):
    return list(filter(lambda num: num > -1, nums))

print(remove_negatives([-1, 3, 4, -99]))