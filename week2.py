# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 20:30:12 2018

@author: Noureddine
"""
import re
data = open('regex_sum_105776.txt')
numlist = list()
for line in data:
    line = line.rstrip()
    numline = re.findall('[0-9]+', line)
    if len(numline) == 0: continue 
    # numlist.append(numline)
    # print(numline)
    num = [int(i) for i in numline]
    # print(num)
    numlist.append(sum(num))
# print the whole sum of numlist    
print(sum(numlist))
    