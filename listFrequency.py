
def listFrequency(xlist):

    flist = []
    for i in range(len(xlist)):
        flist.append(0)
        for j in range(len(xlist)):
            if xlist[i] == xlist[j]:
                flist[i] = flist[i] + 1

    print(flist)


length = int(input("Length of list: "))

xlist1 = list(map(int, input().strip().split()[:length]))

listFrequency(xlist1)

