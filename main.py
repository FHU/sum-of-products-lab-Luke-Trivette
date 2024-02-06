def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be the same length." 
    result = sum(x * y for x, y in zip(list1, list2))
    return result
list1 = list(map(float, input()))
list2 = list(map(float, input()))
output = sum_of_products(list1, list2)
print("Output =", int(output))