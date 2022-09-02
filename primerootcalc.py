from math import sqrt
import os
import time


def write_into_list(x):
    f = open("primes.txt", "a")
    f.write(f'{x},\n')
    f.close()


def better_phi(n):
    result = n  # Initialize result as n

    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while p * p <= n:

        # Check if p is a
        # prime factor.
        if n % p == 0:

            # If yes, then
            # update n and result
            while n % p == 0:
                n = int(n / p)
            result -= int(result / p)
        p += 1

    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most
    # one such prime factor)
    if n > 1:
        result -= int(result / n)
    return result


def is_prime(x):
    if f'{num},\n' in open('primes.txt').read():
        return True
    for i in range(2, int(x / 2) + 1):
        if (num % i) == 0:
            # if factor is found, set flag to True
            return False
    write_into_list(num)
    return True


sum = 0.0
counter = 0
for num in range(3, 10000):
    if is_prime(num):
        phi = better_phi(num - 1)
        print(f'Primzahl: {num}, Generatoren: {phi}')
        sum = sum + phi / (num - 1)
        counter = counter + 1

print(f'Durchschnittlich sind {sum / counter * 100} % der Elemente Generatoren.')