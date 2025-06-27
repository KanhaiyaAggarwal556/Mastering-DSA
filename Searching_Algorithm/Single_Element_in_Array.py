def SingleElement(arr, n):
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]
    low = 0
    high = n - 1
    while low <= high:
        mid = low+ (high - low) // 2
        if arr[mid-1] != arr[mid] != arr[mid+1]:
            return arr[mid]
        elif (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid % 2 == 1 and arr[mid] == arr[mid-1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1
if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the elements of the array: ").split()]
    n = len(arr)
    result = SingleElement(arr, n)
    if result != -1:
        print("The single element in the array is:", result)
    else:
        print("No single element found in the array.")