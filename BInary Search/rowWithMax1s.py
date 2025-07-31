class Solution:
    def lowerBound(self, arr, n, x):
        low, high = 0, n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return n - ans

    def rowWithMax1s(self, arr, n, m):
        max_ones = 0
        index = -1
        for i in range(n):
            ones = self.lowerBound(arr[i], m, 1)
            if ones > max_ones:
                max_ones = ones
                index = i
        return index
