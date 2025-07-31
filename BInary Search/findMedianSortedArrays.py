# Brute Force Approach
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        i=0
        j=0
        k=0
        n1, n2 = len(nums1), len(nums2)
        arr=[0]*(n1+n2)
        while i<n1 and j<n2:
            if nums1[i]<=nums2[j]:
                arr[k]=nums1[i]
                k+=1
                i+=1
            else:
                arr[k]=nums2[j]
                k+=1
                j+=1
        while i<n1:
            arr[k]=nums1[i]
            i+=1
            k+=1
        while j<n2:
            arr[k]=nums2[j]
            j+=1
            k+=1
        if len(arr)%2==0:
            return (arr[len(arr)//2-1]+arr[len(arr)//2])/2
        else:
            return arr[len(arr)//2]
        
# Better Approach
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        med1,med2 = 0,0
        n1,n2 = len(nums1), len(nums2)
        i, j = 0,0 
        cnt = 0
        while i < n1 and j < n2:
            if (cnt-1)*2 == n1+n2 or cnt*2-1 == n1+n2:
                break
            if nums1[i]<nums2[j]:
                cnt+=1
                med2 = med1
                med1 = nums1[i]
                i+=1 
            else:
                med2 = med1
                med1 = nums2[j]
                cnt+=1
                j+=1
        while i < n1:
            if (cnt-1)*2 == n1+n2 or cnt*2-1 == n1+n2:
                break
            cnt+=1
            med2 = med1
            med1 = nums1[i]
            i+=1 
        while j < n2:
            if (cnt-1)*2 == n1+n2 or cnt*2-1 == n1+n2:
                break
            cnt+=1
            med2 = med1
            med1 = nums2[j]
            j+=1 
        print(med1," ", med2)
        return (med1+med2)/2 if (n1+n2)%2 == 0 else med1
        

# Optimized Approach
class Solution:
    def findMedianSortedArrays(self, nums1, nums2   ) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1 = len(nums1)
        n2 = len(nums2)
        low, high = 0, n1
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

