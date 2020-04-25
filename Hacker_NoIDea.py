# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:50:10 2020

@author: sajid ali
"""

# Python3 code to demonstrate working of 
# Identical element summation in lists 
# using sum() + zip() 

# initialize lists 
test_list1 = [1 , 5 , 3] 
test_list2 = [3,1] 

# printing original lists 
print("The original list 1 is : " + str(test_list1)) 
print("The original list 2 is : " + str(test_list2)) 

# Identical element summation in lists 
# using sum() + zip() 
res = sum(x == y for x, y in zip(test_list1, test_list2)) 

# printing result 
print("Summation of Identical elements : " + str(res)) 
