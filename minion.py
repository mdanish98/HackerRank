# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 02:14:30 2020

@author: sajid ali
"""

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import re
def minion(stat,s):
    listVowel = ['a','e','i','o','u','A','E','I','O','U']
    list1 = []
    list2 = []
    list3 = []
    dupList = []
    listScore = []
    #print(s)
    if stat == 0:
        for i in range(0,len(s)):
            if s[i] not in listVowel:
                list1.append(s[i])
    else:
        for i in range(0,len(s)):
            if s[i] in listVowel:
                list1.append(s[i])
    print('Done 1')
    print(list1)   
    for k in list1:
        j = 0 
        for i in range(0,len(s)):
            if s[i] == k:
                list2.append(j)
                break 
            j+=1
    
    print(list2)
    print('Done 2')
    #print(list2)   
    
    for k in list2:
        for i in range(k,len(s)):
            if s[k:i+1] not in list3:
                list3.append(s[k:i+1])
            
    print('Done 3')
    print(list3)
    
    for k in list3:
        listScore.append(len(re.findall('(?='+k+')', s)))
    
    print('Done 4')
    print(list3)
    print(listScore)
    print(sum(listScore))
    
    #return(sum(listScore))
    return 0

st = 'NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANN'
stuart = minion(0,st)
kelvin = minion(1,st)

print(stuart)
print(kelvin)

if stuart > kelvin:
    print('Stuart',stuart)
elif stuart == kelvin:
    print('Draw')
else:
    print('Kelvin',kelvin)

