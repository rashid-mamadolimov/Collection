def solution(A):
    # write your code in Python 3.6
    result = None
    A.sort()
    for i in range(len(A) - 1):
        if A[i] > 0 and A[i+1] - A[i] > 1:
            return A[i] + 1
    if result == None and A[len(A) - 1] >= 0:
        result = A[len(A) - 1] + 1
    else:
        result = 1
    return result

A =  [-1,-3]
print(solution(A))