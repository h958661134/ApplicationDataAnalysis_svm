#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test.py
@time: 2018/5/19 17:42
'''

import csv

with open('测试结果1.csv') as f:
    with open('训练数据集1.csv') as f1:
        f_csv=csv.DictReader(f)
        f1_csv=csv.DictReader(f1)

        allnum1=0
        allnum2=0
        rightnum=0
        for (row,row1) in zip(f_csv,f1_csv):
            # print(type(row1['is_attributed']))
            sign=0
            num=0
            for k in row:
                if k != 'click_time':
                    if row[k]=='1':
                        num+=1
            if num > 3:
                sign=1
            if str(sign) == '1':
                allnum2 += 1
            if row1['is_attributed'] == '1':
                if str(sign) == row1['is_attributed']:
                    rightnum+=1
                allnum1+=1
        print(rightnum*2/(allnum1+allnum2))