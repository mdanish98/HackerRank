# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:57:43 2020

@author: sajid ali
"""

from itertools import permutations

def car_prod(string,length):
    list2 = []
    s = ""
    list1 = list(permutations(string,int(length)))
    for k in list1:
        for i in k:
            s+=i
        list2.append(s)
        s = ""
    list2.sort()
    for z in list2:
        print(z)    
    return 1
    
if __name__=='__main__':
    stri,leng = input().split()
    print(stri,leng)
    car_prod(stri,leng)