#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: csv_01.py
@time: 2018/5/17 19:32
'''

import csv

with open("训练数据集2.csv") as f:
    with open("csv_1.csv", 'w', newline='') as f1:
        with open("csv_0.csv",'w',newline='') as f0:
            f_csv = csv.DictReader(f)
            f_csv1 = csv.writer(f1)
            f_csv0= csv.writer(f0)
            sign0=0
            sign1=0
            headers = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed']
            f_csv1.writerow(headers)
            f_csv0.writerow(headers)
            print(1)
            for row in f_csv:
                list=[]
                if row['is_attributed'] == '0' and sign0<202000:
                    for x in row:
                        if x == 'click_time':
                            newrow=row[x][row[x].find(" ")+1:row[x].find(":")]+row[x][row[x].find(":")+1:]
                            newrow=newrow[:-3]
                            list.append(newrow)
                        elif x == 'attributed_time':
                            pass
                        else:
                            list.append(row[x])
                    f_csv0.writerow(list)
                    sign0+=1
                elif row['is_attributed'] == '1' and sign1<202000:
                    for x in row:
                        if x == 'click_time':
                            newrow = row[x][row[x].find(" ") + 1:row[x].find(":")] + row[x][row[x].find(":") + 1:]
                            newrow = newrow[:-3]
                            list.append(newrow)
                        elif x == 'attributed_time':
                            pass
                        else:
                            list.append(row[x])
                    f_csv1.writerow(list)
                    sign1+=1
