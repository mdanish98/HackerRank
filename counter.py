'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from collections import Counter
cSize = []
cost = []
temp = temp2 = 0

n = int(input()) #10
listSize = list(map(int,input().split())) #[2,3,4,5,6,8,7,6,5,18]
noOfC = int(input()) #6
for i in range(0,noOfC):
    temp,temp2 = input().split()
    cSize.append(int(temp))
    cost.append(int(temp2))
#cSize = [6,6,6,4,18,10]
#cost = [55,55,45,40,60,50]
tot = 0

keyList = list(Counter(listSize).keys())
keyVal = list(Counter(listSize).values())

#print(keyList)
#print(keyVal)
copykeyVal = keyVal.copy()
#print(copykeyVal)
#print(cSize)
#print(cost)
for k in range(0,len(keyList)):
    for z in range(0,len(cSize)):
        if keyList[k]==cSize[z] and copykeyVal[k] != 0:
            tot += cost[z]
            copykeyVal[k] -= 1
            
#print(tot)
