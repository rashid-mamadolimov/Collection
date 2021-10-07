
def allPrimes(x):

    all = []
    allPrimesList = [0]
    for i in range(2, x + 1):
        allPrimesList.append(i)

    while allPrimesList.count(0) > 0:

        for i in range(allPrimesList.count(0)):
            allPrimesList.remove(0)

        for i in range(1, len(allPrimesList)):

            if allPrimesList[i] % allPrimesList[0] == 0:
                allPrimesList[i] = 0

        all.append(allPrimesList[0])
        allPrimesList.pop(0)

    return(all + allPrimesList)


k = int(input("Enter an integer more than 1: "))
print(allPrimes(k))