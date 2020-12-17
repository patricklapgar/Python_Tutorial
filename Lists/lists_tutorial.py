# A list is just a collection of items
# Think of a list as the same thing as an array in other languages

items = ["bananas", "apples", "legos", "books"]

for item in items:
    print(item)

tasks = list(range(1, 10))
print(tasks)

# you can also use negative numbers to iterate through a list backwards
# or to also retrieve indices at the end of the list
print(items[-1]) # prints "books"

# To check if a value is in a list, just use the 'in' keyword
friends = ["Pat", "Alexandra", "Christina"]
"Alexandra" in friends # True
"Leslie" in friends # False

numbers = [1, 2, 3, 4, 5, 7.8, 9]
for num in numbers:
    print(num * num)

# You can also iterate through a list via a while loop
# While loops are typically used when you want to use the information from iterating through a list, like the index. 
numbers = [1, 2, 3, 4, 5, 7.8, 9]
i = 0

while i < len(numbers):
    print(f"{i + 1}: {numbers[i]}")
    i += 1