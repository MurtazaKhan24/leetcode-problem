from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = 0
        while m < len(matrix):
            l,r = 0, len(matrix[m])
            if target >= matrix[m][0] and matrix[m][-1] >= target: 
                while l < r:
                    mid = (l + r) // 2
                    if matrix[m][mid] < target:
                        l += 1
                    elif matrix[m][mid] > target:
                        r -= 1
                    else: 
                        return True
            m += 1
        return False