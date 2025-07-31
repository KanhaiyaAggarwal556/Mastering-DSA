def rootN(x, n):
    if x < 0 and n % 2 == 0:
        return "Invalid input: Even root of negative number is not defined."
    if x == 0 or x == 1:
        return x
    
    low = 0
    high = max(1, x)
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        power = mid ** n
        
        if power == x:
            return mid
        elif power < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
if __name__ == "__main__":
    x = int(input("Enter a non-negative integer to find its nth root: "))
    n = int(input("Enter the value of n (the degree of the root): "))
    result = rootN(x, n)
    print(f"The integer part of the {n}th root of {x} is: {result}")
