# You've built an inflight entertainment system with on-demand movie streaming.

'''
Write a function that takes an integer flight_length (in minutes) 
and a list of integers movie_lengths (in minutes) and 
returns a boolean indicating whether there are two numbers in movie_lengths 
whose sum equals flight_length.
'''

def can_two_movies_fill_flight(movie_lengths, flight_length):
    # Movie lengths we've seen so far
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False

# O(n) time and O(n) space