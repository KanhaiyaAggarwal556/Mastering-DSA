class Solution:
    def shipWithinDays(self, weights, days):
        def totalDays(weights, w):
            days = 0
            cnt = 0
            for i in weights:
                if cnt+i<=w:
                    cnt+=i
                else:
                    days+=1
                    cnt = i
            days+= 1
            return days
    
        low, high = max(weights), sum(weights)
        while low<=high:
            mid = (low+high)//2
            if totalDays(weights, mid) <= days:
                high = mid -1
            else:
                low = mid +1
        return low