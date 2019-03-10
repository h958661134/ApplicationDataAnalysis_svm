#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: signed.py
@time: 2018/5/20 11:07
'''

import csv

with open("G:\\untitled1\\venv\\Include\\xs\\训练数据集2.csv") as f:
    with open("G:\\untitled1\\venv\\Include\\xs\\训练数据集2_predicted_value.csv",'a',newline='') as f1:
        f_csv = csv.DictReader(f)
        f_csv1 = csv.writer(f1)
        headers=['ip','app','device','os','channel','click_time','is_attributed','predicted_value']
        f_csv1.writerow(headers)
        line = 0
        for row in f_csv:
            if line > 557243:
                list2 = []
                list1 = []
                list = []
                list.append(row['ip'])
                list2.append(row['ip'])
                list1.append(prediction(clfip, list))
                list = []
                list.append(row['app'])
                list2.append(row['app'])
                list1.append(prediction(clfapp, list))
                list = []
                list.append(row['device'])
                list2.append(row['device'])
                list1.append(prediction(clfdevice, list))
                list = []
                list.append(row['os'])
                list2.append(row['os'])
                list1.append(prediction(clfos, list))
                list = []
                list.append(row['channel'])
                list2.append(row['channel'])
                list1.append(prediction(clfchannel, list))
                list = []
                newrow = row['click_time'][row['click_time'].find(" ") + 1:row['click_time'].find(":")] + row['click_time'][row['click_time'].find(":") + 1:]
                newrow = newrow[:-3]
                list.append(newrow)
                list2.append(row['click_time'])
                list1.append(prediction(clfct, list))
                list2.append(row['is_attributed'])
                num = 0
                for kk in list1:
                    if kk=='1':
                        num+=1
                if num>3:
                    list2.append('1')
                else:
                    list2.append('0')
                f_csv1.writerow(list2)
            line += 1