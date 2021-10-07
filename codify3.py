def solution(X, A):
    # write your code in Python 3.6
    setA = {A[0]}
    for i in range(1,len(A)):
        setA.add(A[i])
        if len(setA) == X:
           return i

X = 5
A = [1,3,1,4,2,3,5,4]

print(solution(X,A))