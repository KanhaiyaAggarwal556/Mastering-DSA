def minEatingSpeed(piles, h):
    def HoursTaken(piles, h):
        return sum((i+h-1) // h for i in piles)
    low, high = 1, max(piles)
    while low<=high:
        mid = low + (high-low) // 2
        if HoursTaken(piles, mid)<=h:
            high = mid-1
        else:
            low = mid+1
    return low

    