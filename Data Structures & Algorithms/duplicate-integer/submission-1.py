class Solution:
    def hasDuplicate(self, nums):
        sets = {}
        for i in nums:
            if i in sets:
                return True  
            sets[i] = 1  
        return False