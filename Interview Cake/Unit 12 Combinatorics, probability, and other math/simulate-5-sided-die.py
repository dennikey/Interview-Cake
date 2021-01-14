# You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.

'''
rand7() returns each integer with equal probability. 
rand5() must also return each integer with equal probability.
'''

def rand7():
    return 1 # supposed to be random function

def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result

def rand5_2():
    result = rand7()
    return result if result <= 5 else rand5()

# O(infinite) time and O(1) space

'''
write out all the possible results from rand7(), 
and label each one with its final outcome for rand5(). 
Then count up how many ways there are to make each final outcome. 
If the counts aren't the same, the function isn't uniformly random.
'''