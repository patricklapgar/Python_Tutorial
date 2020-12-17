# ask for age
# 18 - 21: wear a wristband
# 21+: drink, normal entry
# else: too young

age = input("How old are you?\n")

# if age:
#     # Python also supports type casting, look below
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter, but you must wear a wristband")
#     elif age >= 21:
#         print("You are good to enter and drink")
#     else:
#         print("You're too young, sorry!")
# else:
#     print("Please enter an age!")

# Another way to write this is with more comparison and logical operators
if age and (age >= 18 and age < 21):
    print("You can enter, but you need a wristband!")
elif age and age >= 21:
    print("You are good to enter and drink!")
else:
    print("You're too young, sorry :(")

# You can also write this in a more efficient way
if age:
    if age >= 21:
        print("You are good to enter and drink!")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't come in, little one! :(")
else:
    print("Please enter an age!")