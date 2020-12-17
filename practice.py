def isEven(num):
    return num % 2 == 0

def partition(arr, fn=isEven):
    truthy_list = []
    falsy_list = []
    for val in arr:
        if fn(val):
            truthy_list.append(val)
        else:
            falsy_list.append(val)
    return [truthy_list, falsy_list]

# ############################################################

