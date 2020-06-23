from functools import reduce

def my_func(p_elem, elem):
    return p_elem * elem


print(reduce(my_func, [elem for elem in range(100, 1001, 2)]))