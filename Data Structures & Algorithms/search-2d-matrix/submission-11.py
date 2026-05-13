class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo = 0
        hi = (m * n) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            cur = matrix[mid // n][mid % n]
            if cur == target:
                return True
            elif cur < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False