def solution(A, K):
    # write your code in Python 3.6
    for j in range(K):
        temp = A[len(A) - 1]
        for i in range(len(A) - 1):
            A[len(A) - 1 - i] = A[len(A) - 2 - i]
        A[0] = temp
    return A

A = [1,2,-2,7,3]
K = 3
solution(A,K)
print(A)


def oddElemOc(A):
    for item in A:
        if A.count(item) % 2 == 1:
            return item

A = [3,4,6,2,7,3,2,7,6]
print(oddElemOc(A))

print(int(2.9))