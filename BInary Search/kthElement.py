    #User function Template for python3


class Solution:

    def kthElement(self, nums1, nums2, k):
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.kthElement(nums2,nums1,k)
        
        low,high = max(k-n2, 0), min(k,n1)
        while low<=high:
            cut1 = (low+high)//2
            cut2 = k - cut1
            
            l1 = float('-inf') if cut1-1 < 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2-1 < 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
        return low
        