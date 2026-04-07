class Solution:
    def trap(self, height) -> int:
        N = len(height)
        
        peak_index = 0
        for i in range(N):
            if height[i] > height[peak_index]:
                peak_index = i

        sum_w = 0
        left_max = 0
        for R in range(peak_index):
            if height[R] > left_max:
                left_max = height[R]
            else:
                sum_w += left_max - height[R]
        
        right_max = 0
        for L in range(N - 1, peak_index, -1):
            if height[L] > right_max:
                right_max = height[L]
            else:
                sum_w += right_max - height[L]

        return sum_w