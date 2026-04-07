class Solution:
    def maxProfit(self, prices):
        ans = []
        loc_max = 0
        l = 0
        r = 1
        while r < len(prices):
            loc_max = max(loc_max, prices[r])
            if prices[r] >= prices[l]:
                ans.append(loc_max - prices[l])
            else:
                l = r
                loc_max = prices[r]
            r += 1
                    
        if ans:
            return max(ans)
        return 0