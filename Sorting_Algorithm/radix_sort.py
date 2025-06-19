def radix_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10

    return arr

if __name__ == "__main__":
    arr = list(map(int, input("Enter non-negative integers (space-separated): ").split()))
    sorted_arr = radix_sort(arr)
    print("Sorted array:", sorted_arr)
