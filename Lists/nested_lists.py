# Nested lists are jus lists inside of other lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested lists are typicall used within complex data structures as well as games
# To access nested lists, use two square brackets side by side
nested_list[0][0] # Returns 1
nested_list[1][-1] # Returns 6

# To iterate over nested lists, you use nested loops
for x in nested_list:
    for num in x:
        print(num)

# There are also nested list comprehensions!! Which are very useful!
# Below is the same code as before, but written as a comprehension
[[print(num) for num in x] for x in nested_list]

# Another example is when you use nested list comprehensions to generate a new nested list
# Below is code that will create small game board
#               
#       Right here is where the           And here is where each of 
#       individual lists are generated    the values are generated
#                   |                       |
#                   V                       V
board = [[num for num in range(1, 4)] for val in range(1, 4)]
print(board)

# Another example
# This is how you use conditional statements within a nested loop comprehension
# 
#       This whole area right here is considered the     Meanwhile, this is the first loop 
#                     'nested loop'                 
#  |                                                |           |
#  V                                                V           V
[["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]

