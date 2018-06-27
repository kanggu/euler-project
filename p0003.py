# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def solve():
    prime_factors = []
    divident = 600851475143
    divisor = 2
    while divisor < 600851475143 and divisor < divident:
        if divident % divisor == 0:
            prime_factors.append(divisor)
            divident = divident / divisor
            print(divisor, "is a factor")
        else:
            divisor += 1
            print(divisor,"is not a factor")
    prime_factors.append(divident)
    return prime_factors[-1]

if __name__ == "__main__":
    print(solve())
