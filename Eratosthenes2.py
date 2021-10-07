def primes(n):

    numbers = []

    for i in range(2, n+1):
        numbers.append(i)

    #print(numbers)

    primes = []

    while len(numbers) > 0:
        prime = numbers[0]
        primes.append(prime)

        for number in numbers:
            if number % prime == 0:
                numbers.remove(number)

    return(primes)

print(primes(5))