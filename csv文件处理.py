#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: test.py
@time: 2018/5/15 13:03
'''

import csv
with open("训练数据集2.csv") as f:
    with open("csv_new1.csv",'w',newline='') as f1:
        f_csv = csv.DictReader(f)
        f_csv1 = csv.writer(f1)
        headers = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'attributed_time', 'is_attributed']
        f_csv1.writerow(headers)
        # for row in f_csv:
        #     list = []
        #     for x in row:
        #         list.append()
        for row in f_csv:
            list=[]
            for x in row:
                list.append(row[x])
            list[5]=list[5][list[5].find(" ")+1:list[5].find(":")]+list[5][list[5].find(":")+1:]
            f_csv1.writerow(list)
