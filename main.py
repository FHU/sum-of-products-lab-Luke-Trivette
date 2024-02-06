def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists must be the same length." 
    x = 0
    result = sum(x * y for x, y in zip(list1, list2))
    return result
list1 = list(map(int, input("Enter the first series of integers: ")))
list2 = list(map(int, input("Enter the second series of integers: ")))
output = sum_of_products(list1, list2)
print("Output =", output)
#oops