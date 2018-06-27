# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def solve():
    total_factors = {}
    for x in range(2, 21):
        individual_factors = get_prime_factors(x)
        for key in individual_factors:
            if key not in total_factors:
                total_factors[key] = individual_factors[key]
            else:
                if individual_factors[key] > total_factors[key]:
                    total_factors[key] = individual_factors[key]
    ans = 1
    for key in total_factors:
        ans = ans * key ** total_factors[key]
    return ans

def get_prime_factors(input):
    prime_factors = {}
    divident = input
    divisor = 2
    while divisor < input and divisor < divident:
        if divident % divisor == 0:
            if divisor in prime_factors:
                prime_factors[divisor] += 1
            else:
                prime_factors[divisor] = 1
            divident = divident / divisor
        else:
            divisor += 1
    if divident in prime_factors:
        prime_factors[divisor] += 1
    else:
        prime_factors[divisor] = 1
    return prime_factors

if __name__ == "__main__":
    print(solve())
