class Solution:
    def trap(self, height) -> int:
        N = len(height)
        R, L = 0, N - 1
        sum_w = 0
        loc_max = [0, 0]
        while R < N:
            if height[R] >= loc_max[1]:
                for char in height[loc_max[0]: R + 1]:
                    count_w = loc_max[1] - char
                    if count_w > 0:
                        sum_w += count_w
                loc_max = [R, height[R]]
            R += 1
        
        peak_index = loc_max[0]
        
        loc_max = [N - 1, 0]
        while L >= peak_index:
            if height[L] > loc_max[1]:
                for char in height[L: loc_max[0] + 1]:
                    count_w = loc_max[1] - char
                    if count_w > 0:
                        sum_w += count_w
                loc_max = [L, height[L]]
            L -= 1

        return sum_w