#! /usr/bin/env python
import sys

def divides(primes, n):
    for trial in primes:
        if n % trial == 0: return True
    return False

def prime_sieve():
    p, current = [], 1
    while 1:
        current += 1
        if not divides(p, current): # if any previous primes divide, cancel
            p.append(current)           # this is prime! save & return
            yield current

if int(sys.argv[1]):
    import psyco
    psyco.full()

import time
t0 = time.time()
for prime in prime_sieve():
    if prime > 100000:
        break
t1 = time.time()

print t1 - t0
