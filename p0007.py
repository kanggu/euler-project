# Problem 7: 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def solve():
    num = 2
    prime_numbers = []
    while len(prime_numbers) < 10001:
        print("Current length: ", len(prime_numbers))
        if is_prime(num):
            print(num, "is prime number")
            prime_numbers.append(num)
        else:
            print(num, "is not prime number")
        num += 1
    return prime_numbers[-1]

def is_prime(input):
    for i in range(2, input):
        if input % i == 0 and i != input:
            return False
    return True

if __name__ == "__main__":
    print(solve())
