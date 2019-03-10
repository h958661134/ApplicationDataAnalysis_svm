#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: svm3.py
@time: 2018/5/17 17:37
'''

# Mathieu Blondel, September 2010
# License: BSD 3 clause

import csv
list = []
with open("训练数据集1.csv") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        if row['ip'] not in list:
            list.append(row['ip'])
    print(len(list))