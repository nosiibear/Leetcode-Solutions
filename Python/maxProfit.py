# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price
# of a given stock on the ith day.
# You want to maximize your profit by choosing a single day
# to buy one stock and choosing a different dat in the future
# to sell that stock.
# Return the maximum profit you can achieve from this transaction.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        min = prices[0]
        total = 0
        for i in range(0, len(prices)):
            print(prices[i])
            print(str(max) + " max")
            print(str(min) + " min")
            print(str(total) + " total")
            print()
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > total:
                total = prices[i] - min
        return total


prices1 = [7, 1, 5, 3, 6, 4]
# 5
prices2 = [7, 6, 4, 3, 1]
# 0
prices3 = [1, 5, 3, 20]
# 19
prices4 = [1, 6, 11, 4, 9, 1]
# 10
prices5 = [1, 2]
# 8
prices6 = [4, 10, 1, 9]

prices7 = [3, 2, 6, 5, 0, 3]
print(Solution.maxProfit("a", prices3))
