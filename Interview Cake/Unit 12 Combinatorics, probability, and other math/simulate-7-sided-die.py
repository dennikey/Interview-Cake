# You have a function rand5() that generates a random integer from 1 to 5. Use it to write a function rand7() that generates a random integer from 1 to 7.

'''
rand5() returns each integer with equal probability. 
rand7() must also return each integer with equal probability.
'''

def rand5():
    return 1 # supposed to be random number 

def rand7_mod():
    return (rand5() + rand5()) % 7 + 1

'''
However, the number of possibilites don't match 7 equally.
5^n or rand5() ^ n doesn't work either since it can't divide evenly with 7.
'''

def rand7_table():
    results = [
        [1, 2, 3, 4, 5],
        [6, 7, 1, 2, 3],
        [4, 5, 6, 7, 1],
        [2, 3, 4, 5, 6],
        [7, 0, 0, 0, 0],
    ]

    while True:
        # Do our die rolls
        row = rand5() - 1
        column = rand5() - 1

        # Case: we hit an extraneous outcome
        # so we need to re-roll
        if row == 4 and column > 0:
            continue

        # Our outcome was fine. return it!
        return results[row][column]

def rand7():
    while True:
        # Do our die rolls
        roll1 = rand5()
        roll2 = rand5()
        outcome_number = (roll1-1) * 5 + (roll2-1) + 1

        # If we hit an extraneous
        # outcome we just re-roll
        if outcome_number > 21:
            continue

        # Our outcome was fine. return it!
        return outcome_number % 7 + 1

# O(infinite) time and O(1) space