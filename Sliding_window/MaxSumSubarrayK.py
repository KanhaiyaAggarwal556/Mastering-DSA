def max_sum_k(arr, k):
    n = len(arr)
    if k > n:
        return -1

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Input section
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter value of k: "))

result = max_sum_k(arr, k)
print("Maximum sum of subarray of length", k, "is:", result)
