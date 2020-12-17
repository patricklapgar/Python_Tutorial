# You can also add conditional logic to list comprehensions which is very useful and powerful
# And the syntax looks like this

numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

# If you're using the 'else' keyword, then the syntax looks a little different
[num*2 if num % 2 == 0 else num/2 for num in numbers]
# Returns [0.5, 4, 1.5, 8, 2.5, 12]

# The next example removes all values from a sentence
with_vowels = "This is so much fun"
result = ''.join(char for char in with_vowels if char not in "aeiou")
print(result)

# An example
def compact(arr):
    """ A function that accepts a list and returns a list of values that have no Falsey values """
    return [value for value in arr if value]

# You can also do this without a list comprehension
# Look below

def compact(arr):
    truthy_values = []
    for value in arr:
        if value: truthy_values.append(value)
    return truthy_values