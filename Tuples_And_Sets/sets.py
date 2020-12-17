# INTRO TO SETS
# Sets are like formal mathematical sets
# They are basically a collection of data that do not have duplicate values
# Elements in a set are NOT ordered
# Because sets are unordered, you cannot access items in a set via its index

# Sets can be useful if you need to keep track of a collection of elements, but don't care about ordering, keys or values and duplicates
# Example
s = set({1, 2, 3, 4, 5, 5, 5}) # Only returns {1, 2, 3, 4, 5}
s = set({1, 4, 5})

# You create sets either with brackets or with the set() function
s = {1, 4, 5}

# You can't access items in set, but you can test to see if a value is in a set
print(4 in s) # Returns True

# Also you can use strings, booleans, and so forth in a set you are not limited to only numbers

# Now, you can access all values in a set by using a for loop
numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print(number)

# A common use case for a set is when you have duplicate values in a list but want to identify the duplicates
cities = {"Dallas", "Houston", "San Antonio", "Dallas", "Galveston", "Paris", "Houston"}
print(list(set(citties)))
print(len(set(cities)))

# ##################################################
# SET METHODS
# ##################################################
# Unlike tuples, sets have a few more important methods associated with them
# The first one is the add() method
# It adds elements to a set
s = set([1, 2, 3])
s.add(4) # Returns {1, 2, 3, 4}

# The next method is the remove() method
# Simply, this method removes elements from a set
set1 = {1, 2, 3, 4, 5, 6}
set1.remove(3) # Returns {1, 2, 4, 5, 6}
# Side note: if you need to avoid keyErrors use the .discard() method to get rid of the values

# Another method is the copy() method.
# This one is also straightforward in that it creates a copy of a the set
set2 = set1.copy()
print(set2)

# Another method to know is the clear() method
# This one removes all contents of the set
set2.clear()

# ################################################
# SET MATH
# ################################################
# Set math is a subset of math
# Sets have quite a few mathematical methods that are important to know
# - intersection
# - symmetric_difference
# - union

# The union method combines two sets and gets rid of all duplicates so that 
# the end result is one set with unique values
# the | operator is a shortcut for unionizing two sets

math_students = {'Patrick', 'Alexandra', 'James', 'Dylan'}
biology_students = {'Patrick', 'Alexandra', 'Christina', 'Tyler', 'Will'}
print(math_students | biology_students) # Returns {'James', 'Patrick', 'Dylan', 'Alexandra', 'Tyler', 'Christina', 'Will'}

# You can also do set intersections, which will return a set of values that are in both sets
# The intersection method uses the & symbol instead of |
print(math_students & biology_students) # Returns {'Alexandra', 'Patrick'}

# ###################################################
# SET COMPREHENSION
# ###################################################
# The concept of set comprehension is the same as list and dictionary comprehensions
# Here's a little example

# Notice that you use brackets just like with dictionary comprehensions
# but you don't specify a key or value
{x**2 for x in range(10)}

# Another example
{char.upper() for char in 'hello'} # Returns {'O', 'L', 'H', 'E'}

# Yet another example is to use these comprehensions in a function
def find_vowels(string):
    # Returns True or False if all vowels are in the string 'aeiou'
    return len({char for char in string if char in 'aeiou'}) == 5

