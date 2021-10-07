def solution(A):
    # write your code in Python 3.6

    mindif = abs(len(A) * max(A))
    print(mindif)
    for p in range(1,len(A)):
        lsum = rsum = 0
        for i in range(p):
            lsum = lsum + A[i]
        print("lsum"+str(lsum))
        for i in range(p,len(A)):
            rsum = rsum + A[i]
        print("rsum"+str(rsum))
        dif = abs(lsum-rsum)
        if dif < mindif:
            mindif = dif
    return mindif

A = [-2,-3,-4,-1]
print(solution(A))