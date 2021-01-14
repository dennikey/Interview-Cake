# You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee

'''
Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
'''

class TempTracker(object):
    def __init__(self):
        # For mode
        self.occurrences = [0] * 111  # List of 0s at indices 0..110
        self.max_occurrences = 0
        self.mode = None

        # For mean
        self.number_of_readings = 0
        self.total_sum = 0.0  # Mean should be float
        self.mean = None

        # For min and max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature):
        # For mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        # For mean
        self.number_of_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.number_of_readings

        # For min and max
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

# O(1) time and O(1) space since possible outcomes are 0-110

'''
Just-in-time - insert() puts the temperatures and generate answers when getters are called
Ahead-of-time - insert() puts and also computes mode, mean, etc - O(1)
There are trade-offs between these two methods
'''