def anz(data,x):
    if len(data) == 1:
        res = data.copy()
    else:

        res_1 = [data[0]]
        res = res_1.copy()
        res_2 = [data[0]]
        for i in range(len(data) - 1):
            if abs(data[i]-data[i+1]) <= x:
                res_2.append(data[i+1])
                res = res_2.copy()
            else:
                if len(res_2) > len(res_1):
                    res = res_2.copy()
                res_1 = res_2.copy()
                res_2.clear()
                res_2.append(data[i+1])

    return res

print(anz([2,7,3,5,6,6,1], 1))
print(anz([2,7,3,5,6,6,1], 2))
print(anz([2,7,3,5,6,6,1], 0))
print(anz([2,7,3,5,6,6,1], 9))
print(anz([3], 2))