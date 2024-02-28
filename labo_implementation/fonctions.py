import random
from math import sqrt
from sympy import isprime
from sympy.ntheory import factorint
import random, sys, os
import pandas as pd
import gmpy2
from math import isqrt
from sympy import *
import math
import math
from sympy import gcd
from sympy import isprime
from sympy import mod_inverse


# Module de cryptomath

# -------------------------------calculer le pgcd:
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


# -------------------------------trouver l'inverse modulaire:

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


# --------------------Module RabinMiller:


import random


def rabinMiller(num,
                k):  # plus vous augmentez k, plus le test est fiable mais prend également plus de temps à s'exécuter.
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(k):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True


# ------------------test de primaliter avc millerRabin:
def isPrime(num):
    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
                 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num, 64)


# ------------------------generation number premier :

def generateLargePrime(keysize):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if isPrime(num):
            return num


# -----------------------generer les cles :

def generate_Key(keySize):
    # Etape 1: crier deux nombres premier p , q et calculer n = p * q:
    print('generation de p')
    p = generateLargePrime(keySize)
    print('generation de q')
    q = generateLargePrime(keySize)
    n = p * q

    # Etape 2: creation de nombre qui est premier avec (p-1)*(q-1):
    print('creation de e')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Etape 3: Calculer d l'inverse de e mode (p-1)*(q-1).
    print('calculer d ')
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    return p, q, n, e, d, (p - 1) * (q - 1)


def isPerfectSquare(n):
    # Vérifie si un nombre est un carré parfait
    s = int(math.sqrt(n))
    return s * s == n


def fermatFactorization(n):
    # Factorisation de Fermat pour factoriser n en deux nombres premiers
    a = int(math.ceil(math.sqrt(n)))
    b2 = a * a - n
    while not isPerfectSquare(b2):
        a += 1
        b2 = a * a - n
    p = a + int(math.sqrt(b2))
    q = a - int(math.sqrt(b2))
    return p, q


def factorize(n):
    # Algorithme de factorisation naïve pour les petits nombres
    if n < 1000:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                p = i
                q = n // i
                if isprime(p) and isprime(q):
                    return p, q
        return None
    if 1000 < n < 10000:
        p, q = fermatFactorization(n)
        return p, q

    # Crible quadratique pour les nombres de taille moyenne
    limit = 10 ** 8
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i ** 2, limit, i):
                primes[j] = False
    for p in range(2, limit):
        if primes[p]:
            if n % p == 0:
                q = n // p
                if isprime(q):
                    return p, q

    # Algorithme GNFS pour les grands nombres

    factors = factorint(n)
    if len(factors) == 2:
        p, q = factors.keys()
        if isprime(p) and isprime(q):
            return p, q

    return None



def wiener_attack(n, e):
    # Fonction pour calculer la fraction continue de e/n
    def continued_fraction_expansion(e, n):
        cf = continued_fraction_iterator(e/n)
        return [nsimplify(frac) for frac in cf]

    # Fonction pour trouver la clé privée à partir des convergents
    def find_private_key(convergents, e):
        for conv in convergents:
            k, d = conv.numerator(), conv.denominator()
            if k != 0 and (e * d - 1) % k == 0:
                phi_n = (e * d - 1) // k
                # Vérifier si phi(n) est pair
                if phi_n % 2 == 0:
                    # Calculer la clé privée
                    x = Symbol('x')
                    roots = solve(x**2 - (n - phi_n + 1) * x + n, x)
                    if len(roots) == 2 and roots[0] * roots[1] == n:
                        return d

        return None

    # Calcul de la fraction continue
    convergents = continued_fraction_expansion(e, n)

    # Recherche de la clé privée parmi les convergents
    private_key = find_private_key(convergents, e)

    return private_key







