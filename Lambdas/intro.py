# Lambdas are a special kind of function
# Here's an example

# A traditional function and function call
def square(num):
    return num * num

print(square(9))

# And here's that same function but with a lambda
# Variable   A lambda is a way to create a function on a single line
# assignment |   
#            |  Pass in parameters
#  |         |     |        Only returns one statement automatically
#  V         V     V        V
square2 = lambda num: num * num
print(square2(7))

# Note: Typically, you do not use lambdas to store as variables

# A common use case for lambdas is when you need to pass in a function as a parameter into another function
