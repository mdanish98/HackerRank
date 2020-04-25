# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:55:52 2020

@author: sajid ali
"""
#n = 5
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((int(((10**i)-1)/9)**2))