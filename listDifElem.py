
def listDifElem(xlist):

    xlist.sort()

    s = 1
    for i in range(len(xlist) - 1):
        if xlist[i] != xlist[i + 1]:
            s = s + 1

    print(s)



xlist1 = []

n = int(input("Length of list: "))

for i in range(n):
    elem = float(input("Element: "))
    xlist1.append(elem)

listDifElem(xlist1)

