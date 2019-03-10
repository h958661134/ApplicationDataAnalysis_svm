#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: svm_处理数据.py
@time: 2018/5/19 11:45
'''
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import csv

def c_in(rowx,rowy,list,y):
    y.append(rowy)
    list.append(rowx)
def prediction(clf,list):
    res = clf.predict([list])
    return res[0]


with open("G:\\untitled1\\venv\\Include\\xs\\csv_0.csv") as f:
    with open("G:\\untitled1\\venv\\Include\\xs\\csv_1.csv") as f1:
        f_csv = csv.DictReader(f)
        f1_csv = csv.DictReader(f1)
        print(f_csv)
        x = []
        y = []
        sign=0
        for (row,row1) in zip(f_csv,f1_csv):
            if sign==50000:
                break
            list = []
            c_in(row['ip'],row['is_attributed'],list,y)
            x.append(list)
            list = []
            c_in(row1['ip'],row1['is_attributed'],list,y)
            x.append(list)
            sign+=1
        print("ip------------------")
        clfip = svm.SVC()  ##默认参数：kernel='rbf'
        clfip.fit(x, y)
        print("ip------------------")

        x = []
        y = []
        sign=0
        for (row,row1) in zip(f_csv,f1_csv):
            if sign==50000:
                break
            list = []
            c_in(row['app'],row['is_attributed'],list,y)
            x.append(list)
            list = []
            c_in(row1['app'],row1['is_attributed'],list,y)
            x.append(list)
            sign+=1
        print("app------------------")
        clfapp = svm.SVC()  ##默认参数：kernel='rbf'
        clfapp.fit(x, y)
        print("app------------------")

        x = []
        y = []
        sign=0
        for (row,row1) in zip(f_csv,f1_csv):
            if sign==50000:
                break
            list = []
            c_in(row['device'],row['is_attributed'],list,y)
            x.append(list)
            list = []
            c_in(row1['device'],row1['is_attributed'],list,y)
            x.append(list)
            sign+=1
        print("device------------------")
        clfdevice = svm.SVC()  ##默认参数：kernel='rbf'
        clfdevice.fit(x, y)
        print("device------------------")

        x = []
        y = []
        sign = 0
        for (row, row1) in zip(f_csv, f1_csv):
            if sign == 50000:
                break
            list = []
            c_in(row['os'], row['is_attributed'], list, y)
            x.append(list)
            list = []
            c_in(row1['os'], row1['is_attributed'], list, y)
            x.append(list)
            sign += 1
        print("os------------------")
        clfos = svm.SVC()  ##默认参数：kernel='rbf'
        clfos.fit(x, y)
        print("os------------------")

        x = []
        y = []
        sign = 0
        for (row, row1) in zip(f_csv, f1_csv):
            if sign == 50000:
                break
            list = []
            c_in(row['channel'], row['is_attributed'], list, y)
            x.append(list)
            list = []
            c_in(row1['channel'], row1['is_attributed'], list, y)
            x.append(list)
            sign += 1
        print("channel------------------")
        clfchannel = svm.SVC()  ##默认参数：kernel='rbf'
        clfchannel.fit(x, y)
        print("channel------------------")

        x = []
        y = []
        sign = 0
        for (row, row1) in zip(f_csv, f1_csv):
            if sign == 50000:
                break
            list = []
            c_in(row['click_time'], row['is_attributed'], list, y)
            x.append(list)
            list = []
            c_in(row1['click_time'], row1['is_attributed'], list, y)
            x.append(list)
            sign += 1
        print("click_time------------------")
        clfct = svm.SVC()  ##默认参数：kernel='rbf'
        clfct.fit(x, y)
        print("click_time------------------")

with open("训练数据集1.csv") as f:
    with open("测试结果1.csv","w",newline='') as f1:
        f_csv = csv.DictReader(f)
        f_csv1 = csv.writer(f1)
        headers=['ip', 'app', 'device', 'os', 'channel', 'click_time']
        f_csv1.writerow(headers)
        list=[]
        for row in f_csv:
            list1=[]
            list = []
            list.append(row['ip'])
            list1.append(prediction(clfip,list))
            list=[]
            list.append(row['app'])
            list1.append(prediction(clfapp, list))
            list = []
            list.append(row['device'])
            list1.append(prediction(clfdevice, list))
            list = []
            list.append(row['os'])
            list1.append(prediction(clfos, list))
            list = []
            list.append(row['channel'])
            list1.append(prediction(clfchannel, list))
            list = []
            list.append(row['click_time'])
            list1.prediction(clfct, list)
            f_csv1.writerow(list1)




