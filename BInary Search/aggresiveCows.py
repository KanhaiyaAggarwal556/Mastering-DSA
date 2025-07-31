class Solution:

    def aggressiveCows(self, stalls, k):
        # your code here
        def settleCows(stalls, k, gap):
            cntCows, last =1, stalls[0]
            for i in range(1,len(stalls)):
                if stalls[i]-last >= gap:
                    cntCows+=1
                    last = stalls[i]
                
                if cntCows==k:
                    return True
            return False
                
        low, high = 1, max(stalls)
        stalls.sort()
        while( low <= high):
            mid = (low+high)//2
            if settleCows(stalls, k, mid):
                low = mid+1
            else:
                high = mid-1
        return high
    