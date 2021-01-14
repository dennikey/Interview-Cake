# A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.

# Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.

'''
There is a better solution than binary approach
Worst case is when first egg breaks in 50th floor and we have to use second egg 49 times to determine the floor
'''

'''
You can also skip 10 floors at a time.
Worst case is use first egg 10 times and second egg 9 times.
'''

'''
breaks 10th floor -> 10 total drops
breaks 20th floor -> 11 total drops
Since max number of drops increases by one each time we skip floors as first egg, you can skip one fewer floor each time you drop the first egg.

1. We want to skip as few floors as possible the first time egg so if the first egg breaks, we don't have many floors for second egg.
2. We want to be able to reduce number of floors we're skipping by one (don't want to go to top and not be able to skip any more)
'''

'''
Equation can be represented by n + (n - 1) + (n - 2) ... + 1 = 100
n = 13.651 ~ 14
'''

'''
Highest floor an egg won't break from
13

Floors we drop first egg from
14

Floors we drop second egg from
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

Total number of drops
14
'''

'''
Highest floor an egg won't break from
98

Floors we drop first egg from
14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99

Floors we drop second egg from
96, 97, 98

Total number of drops
14
'''
