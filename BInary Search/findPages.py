class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        def TotalStudent(arr, pages):
            stn, studentpages = 1, 0
            for i in arr:
                if studentpages+i <= pages:
                    studentpages += i
                else:
                    stn+= 1
                    studentpages = i
            return stn
        if len(arr)<k:
            return -1
        low, high = max(arr), sum(arr)
        while(low<=high):
            mid = (low+high)//2
            stn = TotalStudent(arr, mid)
            if stn>k:
                low = mid + 1
            else:
                high = mid - 1
        return low
