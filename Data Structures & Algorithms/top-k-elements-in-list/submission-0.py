class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = nums.count(num)
            
        return sorted(seen, key = seen.get, reverse = True)[:k]
        
