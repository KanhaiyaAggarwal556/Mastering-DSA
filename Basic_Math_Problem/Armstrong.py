def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
    return x * power(x, y // 2) * power(x, y // 2)

# Function to calculate order of the number
def order(x):
    n = 0
    while x != 0:
        n += 1
        x //= 10
    return n

# Function to check whether the given number is Armstrong number or not
def is_armstrong(x):
    n = order(x)
    temp, total = x, 0
    while temp != 0:
        r = temp % 10
        total += power(r, n)
        temp //= 10
    return total == x

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_armstrong(n):
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")