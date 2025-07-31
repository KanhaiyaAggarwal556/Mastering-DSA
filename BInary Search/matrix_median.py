#User function Template for python3
import bisect
class Solution:
    def median(self, mat):
        def Upper_bound(arr, x):
            return bisect.bisect_right(arr, x)
        def SmallerELements(mat, value, n, m):
            total = 0
            for i in range(n):
                total += Upper_bound(mat[i], value)
            return total
        n, m = len(mat), len(mat[0])
        req = (n * m) // 2
        low, high = min(mat[i][0] for i in range(n)), max(mat[i][m - 1] for i in range(n))
        while low <= high:
            mid = (low + high) // 2
            small_Elem = SmallerELements(mat, mid, n, m)
            if small_Elem <= req:
                low = mid + 1
            else:
                high = mid - 1
        return low