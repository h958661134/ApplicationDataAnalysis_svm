#!/usr/bin/env python
# encoding: utf-8
'''
@author: hanhaotian
@contact: 958661134@qq.com
@software: garner
@file: t.py
@time: 2018/5/22 12:22
'''

def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

if __name__ == "__main__":
    f1,f2,f3=count()
    print(f1())
    print(f2())
    print(f3())