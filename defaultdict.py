# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:34:07 2020

@author: sajid ali
"""

from collections import defaultdict

n,m = input().split()
k = 0
dicta = defaultdict(str)
dictb = defaultdict(str)
for i in range(1,int(n)+1):
    dicta[i] = input()

for j in range(1,int(m)+1):
    dictb[j] = input()

for i in dictb:
    for j in dicta:
        if dictb[i] == dicta[j]:
            print(j, end=' ')
            k += 1
    if k == 0:
        print('-1')
    else:
        print('')
    k = 0
    #listC.append(k)
    #k = 0
    

    