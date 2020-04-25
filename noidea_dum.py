# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:49:39 2020

@author: sajid ali
"""

n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())
print(type(sc_ar))
print(sum([(i in A) - (i in B) for i in sc_ar]))