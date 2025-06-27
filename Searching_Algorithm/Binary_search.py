import bisect
def binary_search(arr, target):
    left, right = 0, len(arr) -1
    arr.sort()  # Ensure the array is sorted before performing binary search
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
# Example usage:
# if __name__ == "__main__":
#     arr = [input("Enter a number: ") for _ in range(int(input("Enter the number of elements: ")))]
#     arr = list(map(int, arr))  # Convert input strings to integers
#     target = int(input("Enter the target number: "))
#     result = binary_search(arr, target)
#     # result = binary_search_recursive(arr, target, 0, len(arr) - 1)
#     if result != -1:
#         print(f"Element found at index {result}")
#     else:
#         print("Element not found in the array")

# Example usage with bisect module
if __name__ == "__main__":
    arr = [int(x) for x in input("Enter sorted numbers separated by space: ").split()]
    target = int(input("Enter the target number: "))
    
    index = bisect.bisect_left(arr, target)
    
    if index < len(arr) and arr[index] == target:
        print(f"Element found at index {index+1} using bisect")
    else:
        print("Element not found in the array using bisect")
