class Solution:
    def smallestDivisor(nums, threshold):
        def totalthreshold(nums, k):
            return sum((i+k-1)//k for i in nums)
        
        low = 1
        high = max(nums)
        while low<=high:
            mid = (high+low)//2

            if totalthreshold(nums, mid) > threshold:
                low = mid + 1
            else:
                high = mid - 1
        return low