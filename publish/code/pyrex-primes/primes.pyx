#
#  Calculate prime numbers
#

def primes(int maxprime):
  cdef int n, k, i
  cdef int p[100000]
  result = []
  k = 0
  n = 2
  while n < maxprime:
    i = 0

    # test against previous primes
    while i < k and n % p[i] <> 0:
      i = i + 1

    # prime? if so, save.
    if i == k:
      p[k] = n
      k = k + 1
      result.append(n)
    n = n + 1

  return result
