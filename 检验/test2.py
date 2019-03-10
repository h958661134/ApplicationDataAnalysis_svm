#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test2.py
@time: 2018/5/19 21:52
'''

import csv

with open("训练数据集2_predicted_value.csv") as f:
    f_csv = csv.DictReader(f)
    line=0
    tureline=0
    for row in f_csv:
        if str(row['predicted_value']) == '1':
            line+=1
        if str(row['is_attributed']) == '1':
            line+=1
            if str(row['is_attributed']) == str(row['predicted_value']):
                tureline+=1
    print(tureline*2/line)

