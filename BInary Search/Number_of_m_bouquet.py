class Solution:
    def minDays(self, bloomDay, m, k):
        def TotalBloomingDays(bloomDay, day, k):
            cnt, ans  = 0, 0 
            for i in bloomDay:
                if(i<=day):
                    cnt+=1
                else:
                    ans+=(cnt//k)
                    cnt = 0
            ans+=cnt//k
            return ans
    
        low, high = min(bloomDay), max(bloomDay)
        while(low<=high):
            mid = (low+high)//2
            bouquets = TotalBloomingDays(bloomDay, mid, k)
            if bouquets >= m:
                high = mid - 1
            else: 
                low = mid + 1
                
        return low if low<=max(bloomDay) else -1  

if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    sol = Solution()
    print(sol.minDays(bloomDay, m, k))  # Output: 3

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/
       

