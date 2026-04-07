class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for i, val in enumerate(nums):
            ost = target - val
            for s in range(i + 1,len(nums)):
                if nums[s] == ost:
                    seen.append(i)
                    seen.append(s)
                    return seen
