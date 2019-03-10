#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test_2.py
@time: 2018/5/20 10:25
'''

import csv

with open("h_csv.csv") as f:
    f_csv = csv.DictReader(f)
    sign=1
    allnum1 = 0
    allnum2 = 0
    numt1 = 0
    for row in f_csv:
        num = 0
        if sign%2==1:
            x=0
        else:
            x=1
        for k in row:
            if row[k] == '1':
                num += 1
        if num >3:
            allnum2 += 1
        if x==1:
            allnum1 += 1
            if num>3:
                numt1 += 1
        sign+=1
    print(numt1*2/(allnum1+allnum2))
