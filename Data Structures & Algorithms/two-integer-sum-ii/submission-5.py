class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        out = []
        while  l < r:
            if nums[l] + nums[r] > t:
                r -= 1
            elif nums[l] + nums[r] < t:
                l += 1
            else:
                out.append(l + 1)
                out.append(r + 1)
                return [l + 1, r + 1]