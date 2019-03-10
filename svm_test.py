#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: svm_test.py
@time: 2018/5/17 13:38
'''

from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt
import csv


x=[]
y=[]
list1=[]
with open("G:\\untitled1\\venv\\Include\\xs\\csv_0.csv") as f:
    f_csv = csv.DictReader(f)
    sign=0
    for row in f_csv:
        # if sign == 100:
        #     break
        list = []
        for k in row:
            if k=='is_attributed':
                y.append(row[k])
                if row[k]=='1':
                    sign+=1
            else:
                list.append(row[k])
        x.append(list)
with open("G:\\untitled1\\venv\\Include\\xs\\csv_1.csv") as f:
    f_csv = csv.DictReader(f)
    sign=0
    for row in f_csv:
        # if sign == 100:
        #     break
        list = []
        for k in row:
            if k=='is_attributed':
                y.append(row[k])
                if row[k]=='1':
                    sign+=1
            else:
                list.append(row[k])
        x.append(list)
print(y)
print(len(y))
clf=svm.SVC()
clf.fit(x,y)

with open("训练数据集1.csv") as f:
    print("预测...")
    f_csv = csv.DictReader(f)
    print("预测数据读完")
    for row in f_csv:
        list = []
        if row['is_attributed'] == '1':
            for k in row:
                if k=='app' or k=='device' or k=='os' or k=='channel':
                    list.append(row[k])
                elif k=='click_time':
                    list.append(row[k][row[k].find(" ")+1:row[k].find(":")])
            list1.append(list)

    res = clf.predict(list1)  ##两个方括号表面传入的参数是矩阵而不是list
    print(res)

    # for i in x:
    #     res = clf.predict(np.array(i).reshape(1, -1))
    #     if res > 0:
    #         plt.scatter(i[0], i[1], c='r', marker='*')
    #     else:
    #         plt.scatter(i[0], i[1], c='g', marker='*')
    #
    # ##生成随机实验数据(15行2列)
    # rdm_arr = np.random.randint(1, 15, size=(len(y), 5))
    # ##回执实验数据点
    # for i in rdm_arr:
    #     res = clf.predict(np.array(i).reshape(1, -1))
    #     print(res)
    #     if res > 0:
    #         plt.scatter(i[0], i[1], c='r', marker='.')
    #     else:
    #         plt.scatter(i[0], i[1], c='g', marker='.')
    # ##显示绘图结果
    # plt.show()



'''
#准备训练样本
x=[[1,8,9],[3,20,2],[1,15,8],[3,35,8],[5,35,1],[4,40,4],[7,80,5],[6,49,6]]
y=[1,1,-1,-1,1,-1,-1,1]

##开始训练
clf=svm.SVC()  ##默认参数：kernel='rbf'
clf.fit(x,y)

print("预测...")
res=clf.predict([[2,2,2]])  ##两个方括号表面传入的参数是矩阵而不是list

##根据训练出的模型绘制样本点
for i in x:
    res=clf.predict(np.array(i).reshape(1, -1))
    if res > 0:
        plt.scatter(i[0],i[1],c='r',marker='*')
    else :
        plt.scatter(i[0],i[1],c='g',marker='*')

##生成随机实验数据(15行2列)
rdm_arr=np.random.randint(1, 15, size=(15,3))
##回执实验数据点
for i in rdm_arr:
    res=clf.predict(np.array(i).reshape(1, -1))
    if res > 0:
        plt.scatter(i[0],i[1],c='r',marker='.')
    else :
        plt.scatter(i[0],i[1],c='g',marker='.')
##显示绘图结果
plt.show()

'''