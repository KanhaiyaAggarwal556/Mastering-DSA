class Solution:
    def findPeakGrid(self, mat):
        def PeakElement(mat, mid, n):
            maxElem,maxInd = -1,-1
            for i in range(n):
                if maxElem < mat[i][mid]:
                    maxElem = mat[i][mid]
                    maxInd = i
            return [maxElem,maxInd]
        n,m = len(mat), len(mat[0])
        low, high = 0, m-1
        while(low<=high):
            mid = (low +high)//2
            poss = PeakElement(mat,mid,n)
            maxElem = poss[0]
            maxInd = poss[1]
            print(poss)
            if mid>0 and maxElem < mat[maxInd][mid-1]:
                high = mid-1
            elif mid+1<m and maxElem < mat[maxInd][mid+1]:
                low = mid+1
            else:
                return [maxInd,mid]
        return [-1,-1]