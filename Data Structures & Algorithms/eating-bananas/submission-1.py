class Solution:
    def get_hours(self, mas, cur, h):
        k = 0
        for obj in mas:
            k += (obj + cur - 1) // cur
        return k <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.get_hours(piles, mid, h):
                hi = mid - 1
            else: 
                lo = mid + 1

        return lo
