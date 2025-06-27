def power_exponentiation(a, b, m):
    result = 1
    a = a % m

    while b > 0:
        if b % 2 == 1:        # If b is odd
            result = (result * a) % m
        a = (a * a) % m
        b //= 2

    return result

# Input section
a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
m = int(input("Enter modulus (m): "))

print(f"Result of ({a}^{b}) % {m} is:", power_exponentiation(a, b, m))
