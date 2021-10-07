"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""

def validity(str_list):
    digits_x = '0123456789-'
    digits = '0123456789'

    val_list = []
    for str in str_list:
        val = 'Valid'
        print(str[0])
        print(str[0])
        if str[0] == '4' or str[0] == '5' or str[0] == '6':
            val = 'Valid'
        else:
            val = 'Invalid'
        if len(str) != 19:
            print(len(str))
            val = 'Invalid'
        for char in str:
            if char not in digits_x:
                val = 'Invalid'
                break
        if str[4] != '-' and str[9] != '-' and str[14] != '-':
            val = 'Invalid'
        x = str[0:4] + str[5:9] + str[10:14] + str[15:19]
        print(x)
        for c in x:
                if c not in digits:
                    val = 'Invalid'
                    break
        for i in range(13):
            if x[i] == x[i+1] and x[i+1] == x[i+2] and x[i+2] == x[i+3]:
                val = 'Invalid'
                break
        val_list.append(val)
    return val_list

print(validity(['5234-1151_1234-1234']))




