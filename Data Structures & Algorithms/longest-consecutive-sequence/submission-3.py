class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ma = 0
        snus = set(nums)
        for num in snus:
            if num - 1 not in snus:
                curr_num = num
                curr_len = 1

                while curr_num + 1 in snus:
                    curr_len += 1
                    curr_num += 1

                ma = max(ma, curr_len)
        return ma
