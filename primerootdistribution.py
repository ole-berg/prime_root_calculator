from math import gcd

import inline as inline
import matplotlib
from numpy import double

import primerootcalc
import matplotlib.pyplot as plt


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
                                                           for powers in range(1, modulo)}]


def is_prime(x):
    for i in range(2, int(x / 2) + 1):
        if (x % i) == 0:
            # if factor is found, set flag to True
            return False
    return True


for n in range(3, 500):
    if is_prime(n):
        print(f'Generatoren der Zahl {n}: {primRoots(n)}')
