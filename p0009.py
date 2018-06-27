# Problem 9: Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def solve():
    # since a + b + c = 1000, so a + b = 1000 - c
    # by squaring both sides, and using a^2 + b^2 = c^2
    # c = 500 - a*b/1000
    # since a < b < c and all of them are natural numbers
    # c is a number smaller than 500, and a*b is divisible by 1000
    for c in range(500, 0, -1): # if there is an answer, c won't reach 0
        for b in range(c-1, 0, -1):
            a = 1000 - b - c
            if is_correct(a,b,c):
                print(a, b, c)
                return a*b*c

def is_correct(a, b, c):
    if (a < b) and (b < c) and (a + b + c == 1000) and a**2 + b**2 == c**2:
        return True
    else:
        return False

if __name__ == "__main__":
    print(solve())
