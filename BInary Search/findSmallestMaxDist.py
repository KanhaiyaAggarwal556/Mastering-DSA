# Brute Force Approach

#User function Template for python3

class Solution:
    def findSmallestMaxDist(self, stations, k):
        # Code here
        n = len(stations)
        howlong = [0] * (n - 1)
        for i in range(k):
            maxSection, maxId = -1, -1
            for j in range(n-1):
                diff = stations[j+1] - stations[j]
                sectionlength =  round(diff / (howlong[j] + 1), 2)
                # print(sectionlength)
                if sectionlength > maxSection:
                    maxSection, maxId = sectionlength, j
            howlong[maxId]+=1
        
        dist = -1
        for i in range(n- 1):
            diff = stations[i+1] - stations[i]
            sectionlength =  round(diff / (howlong[i] + 1), 2)
            dist = max(sectionlength, dist)
        return dist


# Better Approach

#User function Template for python3
import heapq
class Solution:
    def findSmallestMaxDist(self, stations, k):
        # Code here
        n = len(stations)
        pq = []
        howmany = [0]*(n-1)
        for i in range(n-1):
            heapq.heappush(pq, (stations[i]-stations[i+1], i))
        
        for i in range(k):
            secondElem = heapq.heappop(pq)[1]
            howmany[secondElem]+=1
            
            diff = stations[secondElem +1] - stations[secondElem]
            newSecElem = diff / (howmany[secondElem]+1)
            heapq.heappush(pq, (-1*newSecElem, secondElem))
            
        return heapq.heappop(pq)[0]*-1

# Binary Search Approach - Optimized Approach

#User function Template for python3
class Solution:
    def findSmallestMaxDist(self, stations, k):
        # Code here
        def IsPossible(stations, k, n, mid):
            cnt, j = 0, stations[0]
            for i in range(n-1):
                newstations = int((stations[i+1] - stations[i]) / mid)
                cnt += newstations
            return cnt<=k
        n = len(stations)
        low = 0
        high = max(stations[i+1]-stations[i] for i in range(len(stations)-1))
        while high - low > 1e-6:
            mid = (low+high)/2
            if(IsPossible(stations, k, n, mid)):
                high = mid 
            else:
                low = mid 
        return high
            
if __name__ == "__main__":
    # Example usage
    stations = list(map(int, input("Enter station positions: ").split()))
    k = int(input("Enter number of additional stations to add: "))
    
    solution = Solution()
    result = solution.findSmallestMaxDist(stations, k)
    print("Smallest maximum distance after adding stations:", result)
            