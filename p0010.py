# Problem 10: Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def solve(input):
    is_prime = [True for x in range(input)]
    i = 2 # first prime number, to skip 0 and 1
    while i ** 2 <= input:
        if is_prime[i]:
            print(i, "is a prime number")
            for j in range(i * 2, len(is_prime), i): # wipe out multiples of i
                is_prime[j] = False
        i += 1

    ans = 0
    for num in range(2, input):
        if is_prime[num]:
            ans += num
    return ans


if __name__ == "__main__":
    print(solve(2000000))
