def nthPrime(n):

    primes = []
    next = 1

    while len(primes) < n:
        if isPrime(next) == True:
            primes.append(next)
        next = next +1

    return(primes)




import math

def isPrime(x):


    for i in range(2, int(math.sqrt(x)) + 2):

        if x % i == 0 and x != 2 or x ==1:
            r = False
            break
        elif i == int(math.sqrt(x) + 1) or x ==2:
            r = True

    return(r)


print(nthPrime(10))