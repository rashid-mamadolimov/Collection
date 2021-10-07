def doubleStr(strings):
    doubleStrings = []
    for string in strings:
        doubleStrings.append(string[1:])
        doubleStrings.append(string[:len(string) - 1])
    doubleStringsSet = set(doubleStrings)
    newList = list(doubleStringsSet)
    return(newList)

def common(str1, str2):
    res = ''
    if len(str1) > len(str2):
        longStr = str1
        shortStr = [str2]
    else:
        longStr = str2
        shortStr = [str1]

    while res == '' and len(shortStr[0]) >= 1:
        for short in shortStr:
            if short in longStr:
                res = short
        shortStr = doubleStr(shortStr)
    return(res)

print("Common part of strings:", common('qwoer', 'kloehjjk'))
