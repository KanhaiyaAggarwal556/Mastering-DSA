def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Bubble Sort Implementation
if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements (space-separated): ").split()))
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)