#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author: caizhicheng
#Time : 2019/10/13 10:35
#File : functions.py


#和golang一样，函数传参也是浅copy，依据原参的类型决定是值copy还是,不可变类似是值copy，可变类型是指针copy
#和golang一样，[] {}等是可变类型，其他都是不可变，比较好理解
var1="sss"
l={}
def func(var1,list):
    var1="bbb"
    list[var1]="111"
    print(var1,list)

# func(var1,l)
# print(var1,l)



#高阶函数




