

def merge_the_tools(string, k):
    # your code goes here
    strings = []
    for i in range(0,len(string),k):
        strings.append(string[i:i+k])
        for j in range(-1,-len(strings[-1])-1,-1):
            if strings[-1].count(strings[-1][j]) > 1:
                strings[-1] = strings[-1][:j+len(strings[-1])] + ' ' + strings[-1][j+1+len(strings[-1]):]
        strings[-1] = strings[-1].replace(' ','')
    return strings

print(merge_the_tools('AAABCADDEE',5))