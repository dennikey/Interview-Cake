# Writing programming interview questions hasn't made me rich yet ... so I might give up and start trading Apple stocks all day instead.

'''
Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)
'''

def my_get_max_profit(stock_prices):
    max_profit = float('-inf')
    min_price = float('inf')
    for price in stock_prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price  = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit

# O(n) time and O(1) space

'''
What 'additional values' would we need to keep updated as we looked at each item in our input, 
in order to be able to update the 'best answer so far' in constant time?

'best answer so far' - max profit that we can get based on prices
'additional values' - minimum price we've seen so far
-> can be used to calculate max profit by selling now and previous max profit
'''
