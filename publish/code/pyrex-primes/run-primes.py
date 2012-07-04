import primes
l = primes.primes(100000)
assert l[-5:] == [99929, 99961, 99971, 99989, 99991]
print l[-5:]
