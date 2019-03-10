#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: svm_1.py
@time: 2018/5/18 18:16
'''

from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import csv

x=[]
y=[]
list1=[]

with open("G:\\untitled1\\venv\\Include\\xs\\csv_0.csv") as f:
    with open("G:\\untitled1\\venv\\Include\\xs\\csv_1.csv") as f1:
        f_csv = csv.DictReader(f)
        f1_csv=csv.DictReader(f1)
        sign=0
        zip(f_csv,f1_csv)
        for (row,row1) in zip(f_csv,f1_csv):
            if sign == 1000:
                break
            list = []
            y.append(row['is_attributed'])
            list.append(row['click_time'])

            x.append(list)
            list = []
            y.append(row1['is_attributed'])
            list.append(row1['click_time'])
            x.append(list)
            sign+=1
        print("wokaishi")
        clf = svm.SVC()  ##默认参数：kernel='rbf'
        clf.fit(x, y)
        print('over')

res = clf.predict([[1400]])
print(res)

        # for i,j in zip(x,y):
        #     res = clf.predict(np.array(i).reshape(1, -1))
        #     if res == '1':
        #         plt.scatter(i[0],j, c='r', marker='*')
        #     else:
        #         plt.scatter(i[0],j ,c='g', marker='*')
        # plt.gca().axes.get_xaxis().set_visible(False)


        ##生成随机实验数据(15行2列)
        # rdm_arr = np.random.randint(1, 15, size=(1000, 1))
        #回执实验数据点
        # for (i,j) in rdm_arr:
        #     res = clf.predict(np.array(i).reshape(1, -1))
        #     if res == '1':
        #         plt.scatter(i[0], c='r', marker='.')
        #     else:
        #         plt.scatter(i[0], c='g', marker='.')
        ##显示绘图结果
        # plt.show()


