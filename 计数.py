#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: 计数.py
@time: 2018/5/17 19:56
'''

import csv
with open("训练数据集2_predicted_value.csv") as f:
    f_csv = csv.DictReader(f)
    line=0
    for row in f_csv:
        line+=1
    print(line)
    
