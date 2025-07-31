class Solution:
    def midOfMatrix(self, matrix, target):
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        low, high = 0, m
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][n]:
                return mid
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        row = self.midOfMatrix(matrix, target)
        if row == -1:
            return False
        
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
