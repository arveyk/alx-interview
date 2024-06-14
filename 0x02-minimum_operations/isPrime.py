#!/usr/bin/python3
def isPrime(n):
    """Function to determine if a number is prime
    Args:
        n: number to be evaluated
    Returns: True is so, False otherwise
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)

    f = 3
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
        return True

if __name__ == "__main__":
    count = 0
    for i in range(5001):
        if isPrime(i) is True:
            count += 1
            print("{}".format(i), end=", ")
    print("Number of primes{}".format(count))
