def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
def HCF(a, b):
    """Calculate the Highest Common Factor (HCF) of two numbers."""
    return gcd(a, b)
def LCM(a, b):
    """Calculate the Lowest Common Multiple (LCM) of two numbers."""
    return abs(a * b) // gcd(a, b)
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"The GCD of {a} and {b} is {gcd(a, b)}")