
"""
Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for  is not found, print Not found instead.
"""


n = int(input())

name = []
phoneNumber = []
phoneBook = {}
temp = []

for i in range(n):
    temp.clear()
    temp = input().split(" ")
    name.append(temp[0])
    phoneNumber.append(temp[1])
    phoneBook[name[i]] = phoneNumber[i]


query = input()
try:
    while query != "":
        x = phoneBook.get(query)
        if x == None:
            print("Not found")
        else:
            print(query+"="+x)
        query = input()
except EOFError:
    pass
