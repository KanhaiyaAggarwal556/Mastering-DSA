def Minimum_Element_Rotated_Array(arr):
    left, right = 0, len(arr) - 1
    minimum = int(1e9)
    index = -1
    while left <= right:
        mid = left + (right - left) // 2
        
        # Decide which half to search
        if arr[left] <= arr[mid]:  # Left half is sorted
            minimum = min(minimum, arr[left])
            if(minimum == arr[left]):
                index = left
            left = mid + 1
        else:  # Right half is sorted
            minimum = min(minimum, arr[mid])
            if(minimum == arr[mid]):
                index = mid
            right = mid
    
    return index  # The minimum element is at the left pointer

# Example usage:
if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the rotated sorted numbers separated by space: ").split()]
    result = Minimum_Element_Rotated_Array(arr)
    print(f"The minimum element in the rotated array is: {result}")