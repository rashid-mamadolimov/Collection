
def digitsOfInteger(x):
    i = 1
    dig = []

    while x >= 10**(i-1):
        dig.append((x%10**i)//10**(i-1))
        i = i + 1

    dig.reverse()
    if x == 0:
        dig.append(0)
    print(dig)

int1 = int(input("Enter an integer: "))
digitsOfInteger(int1)



