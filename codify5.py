def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return 0
    count =0
    for i in range(len(A) - 1):
        for j in range(i+1,len(A)):
            if A[i] == 0 and A[j] == 1:
                count = count +1
    return count