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
k = 0
for i in listD:
    if i in A:
        h += 1
    if i in B:
        h -= 1

print(h)
