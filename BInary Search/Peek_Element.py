def PeekElement(arr, n):
    if(n == 1):
        return arr[0]
    if(arr[0] >= arr[1]):
        return arr[0]
    if(arr[n - 1] >= arr[n - 2]):
        return arr[n - 1]
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        # Check if mid is a peak element
        if (arr[mid] >= arr[mid - 1]) and (arr[mid] >= arr[mid + 1]):
            return arr[mid]
        
        # If the left neighbor is greater, move to the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
            
        # If the right neighbor is greater, move to the right half
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the elements of the array: ").split()]
    n = len(arr)
    result = PeekElement(arr, n)
    if result != -1:
        print("The peak element in the array is:", result)
    else:
        print("No peak element found in the array.")