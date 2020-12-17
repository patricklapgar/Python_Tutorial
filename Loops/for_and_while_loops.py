# There are two main types of loops to use in python
# The first is the for loop, and the second is the while loop

# Here's the syntax:
# for item in something:
#   do something

# 'item' is a new variable that can be called whatever you want
# It references the current postion of the iterator within what's being looped through

# Example
for char in "hello":
    print(char)

# How to simply iterate through a list (array)
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nums:
    print(i)

# You can also use ranges in for loops
# Ranges are just simple ways to generate numbers to loop over. It's not randomized.
for number in range(1, 8):
    print(number)

# This will print the integers from 0 to 6
for number in range(7):
    print(number)

# The third paramater is called the "step", meaning how many integers to skip and also tells the loop to count up (+) or down (-)
for number in range(1, 10, 2):
    print(number)

nums = range(1, 20, 2)
list(nums)

# New example w/ user input
times = input("How many times do I have to tell you? ")
times = int(times)

for time in range(times):
    print(f"time {time + 1}: CLEAN UP YOUR ROOM")

for x in range(1, 21):
    if x == 4 or x == 13:
        print(f"{x} is unlucky")
    elif x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

# ######################################
# WHILE LOOPS
# ######################################

# while loops continue to execute while a certain condition is truthy,
# and will end when the condition becomes falsy.

# while im_tired:
    # do something

# while loops require more careful setup than for loops, since you have to specify the termination conditions manually
# msg = input("what's the secret password?\n")

# while msg != "bananas":
#     print("WRONG")
#     msg = input("what's the secret password?\n")
# print("CORRECT")

# print("\U0001f600")

# for num in range(1, 11):
#     print("*")

# times = 1
# while times <= 10:
#     print("*")
#     times += 1

# This is how you write nested for loops
# for x in range(3):
#     for num in range(1, 11):
#         print("*" * num)

# for num in range(1, 11):
#     count = 1
#     star = ""
#     while count < num:
#         star += "*"
#         count += 1
#     print(star)

# Another example
# The code below copies and prints whatever the user inputs
msg = input("Say something: ")

while msg != "stop copying me":
    msg = input(f"{msg}\n")
print("FINE... YOU WIN!!")