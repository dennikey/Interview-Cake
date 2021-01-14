# Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome.

"""
"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"""

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1

# O(n) time and O(1) space since there are 128 different characters possible

"""
This is the most common way to get from a brute force approach to something more efficient. Especially for easier problems.
So always ask yourself, right from the start: "Can I save time by using a dictionary?
"""