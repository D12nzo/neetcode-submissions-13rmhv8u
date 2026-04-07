class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                curr_profit = prices[r] - prices[l]
                if curr_profit > max_profit:
                    max_profit = curr_profit
            else:
                l = r
            r += 1

        return max_profit