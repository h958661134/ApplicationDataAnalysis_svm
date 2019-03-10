#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: 数据预处理.py
@time: 2018/5/16 20:56
'''

import csv

def countnum(x,row,numc):
    if row[x] not in numc:
        numc[row[x]]=1
    else:
        numc[row[x]]+=1
    numc['all']+=1

appnum={}
devicenum={}
osnum={}
channelnum={}
click_timenum={}
appnum['all']=0
devicenum['all']=0
osnum['all']=0
channelnum['all']=0
click_timenum['all']=0
#创建字典

with open("csv_new1.csv") as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        list = []
        for x in row:
            list.append(x)
        break
    for row in f_csv:
        list=[]
        for x in row:
            if x == 'app':
                countnum('app',row,appnum)
            if x == 'device':
                countnum('device',row,devicenum)
            if x == 'os':
                countnum('os',row,osnum)
            if x == 'channel':
                countnum('channel',row,channelnum)
            if x == 'click_time':
                countnum('click_time',row,click_timenum)
#写入字典

with open("csv_new1.csv") as f:
    with open("csv_new12.csv", 'w', newline='') as f1:
        f_csv = csv.DictReader(f)
        f_csv1 = csv.writer(f1)
        headers = ['app', 'device', 'os', 'channel', 'click_time', 'is_attributed']
        f_csv1.writerow(headers)
        for row in f_csv:
            list = []
            for x in row:
                if x=='app':
                    list.append(appnum[row[x]]/appnum['all'])
                if x == 'device':
                    list.append(devicenum[row[x]]/devicenum['all'])
                if x == 'os':
                    list.append(osnum[row[x]]/osnum['all'])
                if x == 'channel':
                    list.append(channelnum[row[x]]/channelnum['all'])
                if x == 'click_time':
                    list.append(click_timenum[row[x]]/click_timenum['all'])
                if x == 'is_attributed':
                    list.append(row[x])
            f_csv1.writerow(list)