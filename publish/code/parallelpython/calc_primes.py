#!/usr/bin/python
import sys, time
import pp

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    import math
    
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2, n) if isprime(x)])

####

# Creates jobserver with specified number of workers
job_server = pp.Server(ncpus=int(sys.argv[1]))

print "Starting pp with", job_server.get_ncpus(), "workers"

start_time = time.time()

# Submit a job of calulating sum_primes(100) for execution.
#
#    * sum_primes - the function
#    * (input,) - tuple with arguments for sum_primes
#    * (isprime,) - tuple with functions on which function sum_primes depends
#
# Execution starts as soon as one of the workers will become available

inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)

jobs = []
for input in inputs:
    job = job_server.submit(sum_primes, (input,), (isprime,))
    jobs.append(job)

for job, input in zip(jobs, inputs):
    print "Sum of primes below", input, "is", job()

print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()
