# Find a duplicate, Space Edition

'''
We have a list of integers, where:

The integers are in the range 1..n
The list has a length of n+1

It follows that our list has at least one integer which appears at least twice. But it may have several duplicates, 
and each duplicate may appear more than twice.

Write a function which finds an integer that 
appears more than once in our list.
'''

'''
def find_repeat(numbers):
    numbers_seen = set()
    for number in numbers:
        if number in numbers_seen:
            return number
        else:
            numbers_seen.add(number)

    # Whoops--no duplicate
    raise Exception('no duplicate!')

but O(n) time and O(n) space
'''

'''
def find_repeat_brute_force(numbers):
    for needle in range(1, len(numbers)):
        has_been_seen = False
        for number in numbers:
            if number == needle:
                if has_been_seen:
                    return number
                else:
                    has_been_seen = True

    # Whoops--no duplicate
    raise Exception('no duplicate!')

but O(n^2) time and O(1) space
'''

'''
Sort the list and find the adjacent values

but O(nlgn) time and O(1) space
'''

'''
1. Find the number of integers in our input list which lie within the range 1..n/2 
2. Compare that to the number of possible unique integers in the same range
3. If the number of actual integers is greater than the number of possible integers, 
we know there’s a duplicate in the range 1..n/2, so we iteratively use the same approach on that range
4. If the number of actual integers is not greater than the number of possible integers, we know 
there must be duplicate in the range n/2 + 1..n, so we iteratively use the same approach on that range
5. At some point, our range will contain just 1 integer, which will be our answer
'''

def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
            lower_range_ceiling
            - lower_range_floor
            + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor

# O(1) space and O(nlgn) time
