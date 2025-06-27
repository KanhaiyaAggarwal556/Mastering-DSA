def Rotated_Search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target is in the left half
            else:
                left = mid + 1   # Target is in the right half
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1   # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half
    
    return -1  # Target not found

def search_rotated_array_duplicates(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Handle duplicates
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
# Example usage:
if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the rotated sorted numbers separated by space: ").split()]
    target = int(input("Enter the target number: "))
    # result = Rotated_Search(arr, target)
    result = search_rotated_array_duplicates(arr, target)
    if result != -1:    
        print(f"Element found at index {result}")
    else:
        print("Element not found in the array")    