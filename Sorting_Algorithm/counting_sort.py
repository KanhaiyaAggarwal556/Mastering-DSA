def counting_sort(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Step 1: Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Step 2: Build the sorted array
    index = 0
    for i in range(range_size):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1

    return arr

# I/O
if __name__ == "__main__":
    arr = list(map(int, input("Enter integers (space-separated): ").split()))
    sorted_arr = counting_sort(arr)
    print("Sorted array:", sorted_arr)
    