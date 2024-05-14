import numpy as np



def print_array_item(array):
    for item in array:
        print(item)

a = np.array([1,2,3])

print_array_item(a)


total = np.sum(a)
print(total)

product = a*3
print(product)