# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:44:42 2020

@author: sajid ali
"""
'''
n = int(input())
set1 = list(map(int,input().split()))
set2 = set(set1)        
print(sum(set2)/len(set2))
myset = set()
myset.update({1, 6}, (5, 13))
#myset.discard(10)
myset.remove(10)
print(myset)

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

m = int(input())
seta = set(map(int,input().split()))
n = int(input())
setb = set(map(int,input().split()))
set1 = set()
set1.update(seta.difference(setb))
set1.update(setb.difference(seta))
#print(sorted(set1))
for i in sorted(set1):
    print(i)
#print(a.union(b))
#print(a.intersection(b))
#print(b.difference(a))

set1 = set([2,3,4,4])
print(set1.pop())
print(type(set1))
'''

l1 = set([1,2,3,4,5,6,7,8,9])
for i in range(0,3):
    m = input().split(' ')
    if len(m) == 1:
        l1.pop()
    elif m[0] == 'remove':
        l1.remove(int(m[1]))
    elif m[0] == 'discard':
        l1.discard(int(m[1]))
print(l1)       
#print(type(m))
