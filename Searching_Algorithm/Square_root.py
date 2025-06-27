def SquareRoot(x):
    if x < 0:
        return "Invalid input: Square root of negative number is not defined."
    if x == 0 or x == 1:
        return x
    
    low = 0
    high = x
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
if __name__ == "__main__":
    x = int(input("Enter a non-negative integer to find its square root: "))
    result = SquareRoot(x)
    print(f"The integer part of the square root of {x} is: {result}")