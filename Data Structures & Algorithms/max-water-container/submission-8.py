class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ma = -10 ** 10
        for i in range(len(heights)):
            for j in range(len(heights) - 1, -1, -1):
                if j > i:
                    hi = min(heights[j], heights[i])
                    ma = max(ma, hi * (j - i))
        return ma