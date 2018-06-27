# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def solve():
    palindromic_numbers = []
    for i in range(999, 199, -1):
        for j in range(999, 199, -1):
            if is_palindrome(i * j):
                palindromic_numbers.append(i * j)
    return max(palindromic_numbers)

def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(solve())
