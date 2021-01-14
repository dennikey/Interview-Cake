# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

'''
[1, 7, 3, 4] would give [84, 12, 28, 21] or [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
'''

'''
1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5 -> 1, 1*2, 1*2*6, 1*2*6*5

The product of all the integers except the integer at each index can be broken down into two pieces:

the product of all the integers before each index, and
the product of all the integers after each index
'''

# need division by zero
def my_get_products_of_all_ints_except_at_index(int_list):
    ans = 1

    for i in int_list:
        ans *= i

    ans_arr = [ans] * len(int_list)

    for counter, i in enumerate(int_list):
        ans_arr[counter] /= i

    print(ans_arr)

def get_products_of_all_ints_except_at_index(int_list):
    
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in range(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index

# O(n) time and O(n) space

'''
Start with a brute force solution, 
look for repeat work in that solution, 
and modify it to only do that work once.
'''