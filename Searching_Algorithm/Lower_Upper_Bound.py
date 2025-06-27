import bisect
def lower_bound(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low
def upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    return low
# Example usage:
# if __name__ == "__main__":
#     arr = [int(x) for x in input("Enter sorted numbers separated by space: ").split()]
#     target = int(input("Enter the target number: "))
    
#     lb = lower_bound(arr, target)
#     ub = upper_bound(arr, target)
    
#     print(f"Lower bound index of {target}: {lb}")
#     print(f"Upper bound index of {target}: {ub}")
    
#     if lb < len(arr) and arr[lb] == target:
#         print(f"Lower bound value: {arr[lb]}")


#     else:
#         print("Target not found in the array for lower bound.")
    
#     if ub > 0 and ub - 1 < len(arr) and arr[ub - 1] == target:
#         print(f"Upper bound value: {arr[ub - 1]}")
#     else:
#         print("Target not found in the array for upper bound.")

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter sorted numbers separated by space: ").split()]
    target = int(input("Enter the target number: "))
    
    lb = bisect.bisect_left(arr, target)
    ub = bisect.bisect_right(arr, target)
    print(f"Lower bound index of {target}: {lb}")
    print(f"Upper bound index of {target}: {ub-1}")
    if lb < len(arr) and arr[lb] == target:
        print(f"Lower bound value: {arr[lb]}")
    else:
        print("Target not found in the array for lower bound.")
    if ub > 0 and ub - 1 < len(arr) and arr[ub - 1] == target:
        print(f"Upper bound value: {arr[ub - 1]}")
    else:
        print("Target not found in the array for upper bound.")
    