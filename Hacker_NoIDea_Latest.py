# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:38:46 2020

@author: sajid ali
"""
from collections import Counter
# Enter your code here. Read input from STDIN. Print output to STDOUT
h = 0
n,m = input().split()
listD = list(input().split())
A = set(input().split())
B = set(input().split())
intAD = ()
intBD = ()
intADBD = ()
'''
#listD = list(Counter(listD).keys())
for i in listD:
    h = h + (i in A) - (i in B)

        
'''
k = 0
#print(len(listD))
for i in listD:
    if i in A:
        k += 1
    if i in B:
        k -= 1
    h += k
    k = 0

'''
intAD = A.intersection(listD)
intBD = B.intersection(listD)
h = len(A.intersection(listD))

#print(intAD)
#print(intBD)
#intADBD = intAD.intersection(intBD)
h = h - len(intBD)




'''
'''
lA = 0
lB = 0
lA = len(A.intersection(listD))
lB = len(B.intersection(listD))
h = lA - lB
'''
'''
for i in listD:
    if i in A:
        h += 1
    if i in B:
        h -= 1

'''
'''
for i in A:
    cA = listD.count(i)
for j in B:
    cB = listD.count(j)
print(cA - cB)

'''
print(h)
