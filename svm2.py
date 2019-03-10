#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: svm2.py
@time: 2018/5/17 13:55
'''
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

#准备训练样本
x=[[1,8,9],[3,20,2],[1,15,8],[3,35,8],[5,35,1],[4,40,4],[7,80,5],[6,49,6]]
y=[1,1,-1,-1,1,-1,-1,1]

##开始训练
clf=svm.SVC()  ##默认参数：kernel='rbf'
clf.fit(x,y)

print("预测...")
res=clf.predict([[2,2,2]])  ##两个方括号表面传入的参数是矩阵而不是list
print(res[0])

##根据训练出的模型绘制样本点
# for i in x:
#     res=clf.predict(np.array(i).reshape(1, -1))
#     if res > 0:
#         plt.scatter(i[0],i[1],c='r',marker='*')
#     else :
#         plt.scatter(i[0],i[1],c='g',marker='*')
#
# ##生成随机实验数据(15行2列)
# rdm_arr=np.random.randint(1, 15, size=(15,3))
# ##回执实验数据点
# for i in rdm_arr:
#     res=clf.predict(np.array(i).reshape(1, -1))
#     if res > 0:
#         plt.scatter(i[0],i[1],c='r',marker='.')
#     else :
#         plt.scatter(i[0],i[1],c='g',marker='.')
# ##显示绘图结果
# plt.show()