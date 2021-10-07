def allPrimes(n):
    primes = [2]
    next = 3
    while len(primes) < n:
    #while primes[len(primes) - 1] < n:
        isPrime = True
        for prime in primes:
            if next % prime == 0:
                isPrime = False
        if isPrime == True:
            primes.append(next)
        next = next + 1
    #primes.pop(len(primes) - 1)
    return primes


n = int(input("Enter an integer: "))
print(allPrimes(n))