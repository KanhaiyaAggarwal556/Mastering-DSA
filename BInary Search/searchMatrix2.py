# Brute Force Approach
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in matrix:
            for j in i:
                if j==target:
                    return True

        return False
# Better Approach
class Solution:
    def rowBinarySearch(self, row, target):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix, target):
        for row in matrix:
            if self.rowBinarySearch(row, target):
                return True
        return False
# Optimized Approach
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row = 0
        col = len(matrix[0])-1
        while row<len(matrix) and col>=0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row+=1
            else:
                col-=1
        return False
